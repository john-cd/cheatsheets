// TODO Reviewed ??-??-2026

var INPUT_DATABASE_NAME = "inputDB";
var OUTPUT_DATABASE_NAME = "outputDB";
var STATS_COLLECTION_NAME = "stats";

function normalizeAddressKey(address) {
    return (address || "").toString().toLowerCase();
}

function buildStatsAggregationPipeline(limit) {
    var max = Number.isInteger(limit) && limit > 0 ? limit : 100000;
    return [
        { $group: { _id: { $toLower: "$address" }, count: { $sum: 1 } } },
        { $sort: { "count": -1 } },
        { $limit: max },
        { $out: { db: OUTPUT_DATABASE_NAME, coll: STATS_COLLECTION_NAME } }
    ];
}

function gatherStats() {
    var start = Date.now();

    var inputDB = db.getSiblingDB(INPUT_DATABASE_NAME);
    var inputColl = inputDB.getCollection("inputColl");

    var outputDB = db.getSiblingDB(OUTPUT_DATABASE_NAME);

    // $out writes to outputDB and atomically replaces its stats collection.
    inputColl.aggregate(buildStatsAggregationPipeline(100000), { allowDiskUse: true }); // Returns { _id, count } where _id is the address.

    var statsColl = outputDB.getCollection(STATS_COLLECTION_NAME);

    // Rebuilding the derived collection makes repeated runs idempotent.
    var outputColl = outputDB.getCollection("outputColl");
    outputColl.deleteMany({});
    var outputBulk = outputColl.initializeUnorderedBulkOp();
    var counter = 0;

    var inputCursor = inputColl.find( {}, {} );
    inputCursor.forEach( function(doc) {
        var statDoc = statsColl.findOne( { _id: normalizeAddressKey(doc.address) } );
        if (statDoc) {
            doc.count = statDoc.count;
            outputBulk.insert(doc);
            counter++;
            if ( counter % 1000 == 0 ) {
                    outputBulk.execute();
                    // You have to reset.
                    outputBulk = outputColl.initializeUnorderedBulkOp();
                }
            }
        }
    );

    if ( counter % 1000 > 0 )
        outputBulk.execute();


    // Print the results.
    outputColl.find({}).sort({count: -1}).forEach(printjson);

    var end = Date.now();
    var duration = (end - start)/1000;
    console.log("Duration: " + duration + " seconds");

    console.log(" | DONE | ");
}

if (typeof module !== "undefined" && module.exports) {
    module.exports = { gatherStats, normalizeAddressKey, buildStatsAggregationPipeline };
}

if (typeof module === "undefined" || !module.parent) {
    gatherStats();
}
