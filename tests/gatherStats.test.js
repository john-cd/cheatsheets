const test = require("node:test");
const assert = require("node:assert/strict");
const {
  normalizeAddressKey,
  buildStatsAggregationPipeline,
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
  assert.equal(pipeline[3].$out, "stats");
});

test("buildStatsAggregationPipeline defaults to safe max", () => {
  const pipeline = buildStatsAggregationPipeline(0);
  assert.equal(pipeline[2].$limit, 100000);
});
