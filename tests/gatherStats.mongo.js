// Disposable MongoDB integration fixture. This script drops inputDB and outputDB.
// Run from the repository root with:
// mongosh --quiet --eval 'GATHER_STATS_TEST_ACK = "disposable"; load("tests/gatherStats.mongo.js")'
if (
    typeof GATHER_STATS_TEST_ACK === "undefined" ||
    GATHER_STATS_TEST_ACK !== "disposable"
) {
    throw new Error("Refusing to run without the disposable MongoDB acknowledgement.");
}

var inputDB = db.getSiblingDB("inputDB");
var outputDB = db.getSiblingDB("outputDB");

inputDB.dropDatabase();
outputDB.dropDatabase();

inputDB.inputColl.insertMany([
    { _id: 1, address: "Alice", value: 10 },
    { _id: 2, address: "ALICE", value: 20 },
    { _id: 3, address: "Bob", value: 30 }
]);
outputDB.outputColl.insertOne({ _id: "stale", address: "stale", count: 99 });

load("docs/includes/gatherStats.js");
gatherStats();

assert.eq(2, outputDB.stats.countDocuments({}));
assert.eq(2, outputDB.stats.findOne({ _id: "alice" }).count);
assert.eq(1, outputDB.stats.findOne({ _id: "bob" }).count);
assert.eq(3, outputDB.outputColl.countDocuments({}));
assert.eq(0, outputDB.outputColl.countDocuments({ _id: "stale" }));
assert.eq(-1, inputDB.getCollectionNames().indexOf("stats"));

gatherStats();

assert.eq(2, outputDB.stats.countDocuments({}));
assert.eq(3, outputDB.outputColl.countDocuments({}));
assert.eq(0, outputDB.outputColl.countDocuments({ _id: "stale" }));
print("gatherStats MongoDB integration checks passed");
