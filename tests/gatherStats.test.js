// TODO Reviewed ??-??-2026

const test = require("node:test");
const assert = require("node:assert/strict");
const {
  normalizeAddressKey,
  buildStatsAggregationPipeline,
  gatherStats,
} = require("../docs/includes/gatherStats.js");

test("normalizeAddressKey lowercases and stringifies values", () => {
  assert.equal(normalizeAddressKey("AbC"), "abc");
  assert.equal(normalizeAddressKey(123), "123");
  assert.equal(normalizeAddressKey(undefined), "");
});

test("buildStatsAggregationPipeline creates expected aggregation", () => {
  const pipeline = buildStatsAggregationPipeline(5);
  assert.equal(Array.isArray(pipeline), true);
  assert.equal(pipeline[0].$group._id.$toLower, "$address");
  assert.equal(pipeline[2].$limit, 5);
  assert.deepEqual(pipeline[3].$out, { db: "outputDB", coll: "stats" });
});

test("buildStatsAggregationPipeline defaults to safe max", () => {
  const pipeline = buildStatsAggregationPipeline(0);
  assert.equal(pipeline[2].$limit, 100000);
});

test("gatherStats writes stats to outputDB and replaces prior output rows", () => {
  const inputDocuments = [
    { _id: 1, address: "Alice", value: 10 },
    { _id: 2, address: "ALICE", value: 20 },
    { _id: 3, address: "Bob", value: 30 },
  ];
  const stats = new Map();
  const outputDocuments = [{ _id: "stale", count: 99 }];
  const databases = new Map();
  const inputCollection = {
    aggregate(pipeline) {
      const output = pipeline.at(-1).$out;
      assert.deepEqual(output, { db: "outputDB", coll: "stats" });
      const grouped = new Map();
      for (const document of inputDocuments) {
        const key = normalizeAddressKey(document.address);
        grouped.set(key, (grouped.get(key) || 0) + 1);
      }
      stats.clear();
      for (const [key, count] of grouped) {
        stats.set(key, { _id: key, count });
      }
    },
    find() {
      return {
        forEach(callback) {
          inputDocuments.forEach((document) => callback({ ...document }));
        },
      };
    },
  };
  const outputCollection = {
    deleteMany() {
      outputDocuments.length = 0;
    },
    initializeUnorderedBulkOp() {
      const pending = [];
      return {
        insert(document) {
          pending.push(document);
        },
        execute() {
          outputDocuments.push(...pending);
        },
      };
    },
    find() {
      return {
        sort() {
          return {
            forEach(callback) {
              [...outputDocuments]
                .sort((left, right) => right.count - left.count)
                .forEach(callback);
            },
          };
        },
      };
    },
  };

  databases.set("inputDB", {
    getCollection(name) {
      assert.equal(name, "inputColl");
      return inputCollection;
    },
  });
  databases.set("outputDB", {
    getCollection(name) {
      if (name === "stats") {
        return {
          findOne(query) {
            return stats.get(query._id) || null;
          },
        };
      }
      assert.equal(name, "outputColl");
      return outputCollection;
    },
  });

  const previousDb = global.db;
  const previousPrintjson = global.printjson;
  const previousLog = console.log;
  const shellDb = {
    getSiblingDB(name) {
      assert.ok(databases.has(name), `unexpected database: ${name}`);
      return databases.get(name);
    },
  };
  global.db = shellDb;
  global.printjson = () => {};
  console.log = () => {};

  try {
    gatherStats();
    assert.equal(global.db, shellDb, "gatherStats must not change the shell's current database");
    assert.equal(stats.has("alice"), true);
    assert.equal(stats.has("bob"), true);
    assert.equal(outputDocuments.length, 3);
    assert.deepEqual(
      outputDocuments.map(({ address, count }) => [address, count]),
      [
        ["Alice", 2],
        ["ALICE", 2],
        ["Bob", 1],
      ],
    );

    gatherStats();
    assert.equal(global.db, shellDb, "repeat runs must preserve the shell's current database");
    assert.equal(outputDocuments.length, 3);
    assert.equal(outputDocuments.some(({ _id }) => _id === "stale"), false);
  } finally {
    global.db = previousDb;
    global.printjson = previousPrintjson;
    console.log = previousLog;
  }
});
