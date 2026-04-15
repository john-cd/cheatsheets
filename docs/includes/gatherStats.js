function normalizeAddressKey(address) {
    return (address || "").toString().toLowerCase();
}

function buildStatsAggregationPipeline(limit) {
    var max = Number.isInteger(limit) && limit > 0 ? limit : 100000;
    return [
        { $group: { _id: { $toLower: "$address" }, count: { $sum: 1 } } },
        { $sort: { "count": -1 } },
        { $limit: max },
        { $out: "stats" }
    ];
}

function gatherStats() {
    var start = Date.now();

    var inputDB = db.getSiblingDB("inputDB");
    var inputColl = inputDB.getCollection("inputColl");

    // Debug: inputColl.find( {} ).limit(2).forEach(printjson).

    outputDB = db.getSiblingDB("outputDB");
    db = outputDB; // Set current database for the next aggregate step.

    // Create temporary collection with count.
    inputColl.aggregate(buildStatsAggregationPipeline(100000), { allowDiskUse: true }); // Returns { _id, count } where _id is the address.

    var statsColl = outputDB.getCollection("stats");

   // Create output collection.
    var outputColl = outputDB.getCollection("outputColl");
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
