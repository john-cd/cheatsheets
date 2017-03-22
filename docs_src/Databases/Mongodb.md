---
title: MongoDB Cheatsheet
category: databases
tags: NoSQL
comments: true
---

## Import from CSV

```bash
mongoimport --db users --collection contacts --type csv --headerline --file contacts.csv
```

Specifying `--headerline` instructs mongoimport to determine the name of the fields using the first line in the CSV file.
Use the `--ignoreBlanks` option to ignore blank fields. For CSV and TSV imports, this option provides the desired functionality in most cases, because it avoids inserting fields with null values into your collection.

[MongoImport documentation](https://docs.mongodb.org/manual/reference/program/mongoimport/ )

## Print from a Cursor

```js
myCursor.forEach(printjson);

// or
while (myCollection.hasNext()) {
   printjson(myCollection.next());
} 
```

## Aggregation Tips

```js
// lowercase a string 
{ $project: { "address": { $toLower: "$address" } } },

// extract field within embedded document
{ $project: { "experience.location": 1 } },

// flatten 
{ $unwind: "$experience"},
{ $group: { _id: "$_id", locs: { $push: { $ifNull: [ "$experience.location", "undefined" ] } } } }
 
// output a collection
{ $out: "myCollection2" }

// get unique values 
{ $group: { _id: "$fulladdress" } }
```

## Make a Copy

Don't use copyTo - it is fully blocking... and deprecated in 3.x

- Use the Aggregation framework:

```js
db = db.getSiblingDB("myDB"); // set current db for $out
var myCollection = db.getCollection("myCollection");

// project if needed, get uniques if needed, create a new collection
myCollection.aggregate([{ $project:{ "fulladdress": 1 } },{ $group:{ _id: "$fulladdress" } },{ $out: "outputCollection" }], { allowDiskUse:true }); 
```

- Or use bulk update:

```js
var outputColl = db.getCollection( "outputCollection" );
var outputBulk = outputColl.initializeUnorderedBulkOp();
myCollection.find( {}, { "fulladdress": 1 } ).forEach( function(doc) {
     outputBulk.insert(doc);
});
outputBulk.execute();
```

## Longer Example

Add a count field to all records

```js
function gatherStats() {   
    var start = Date.now();
    
    var inputDB = db.getSiblingDB("inputDB");
    var inputColl = inputDB.getCollection("inputColl");

    // debug: inputColl.find( {} ).limit(2).forEach(printjson);  

    outputDB = db.getSiblingDB("outputDB"); 
    db = outputDB; // set current database for the next aggregate step

    // create temporary collection with count
    inputColl.aggregate(  [ 
    { $group: { _id: { $toLower: "$address" }, count: { $sum: 1 } } }, 
    { $sort: { "count": -1 } },
    { $limit: 100000 },                 // limit to 100k addresses with highest count  
    { $out: "stats" }
    ],  { allowDiskUse: true } );       // returns { _id, count } where _id is the address

    var statsColl = outputDB.getCollection("stats");
    
   // create output collection
    var outputColl = outputDB.getCollection("outputColl"); 
    var outputBulk = outputColl.initializeUnorderedBulkOp(); 
    var counter = 0; 
    
    var inputCursor = inputColl.find( {}, {} ); 
    inputCursor.forEach( function(doc) { 
        var statDoc = statsColl.findOne( { _id: doc.address } );
        if (statDoc) {
            doc.count = statDoc.count;
            outputBulk.insert(doc);
            counter++;  
            if ( counter % 1000 == 0 ) {
                    outputBulk.execute();
                    // you have to reset
                    outputBulk = outputColl.initializeUnorderedBulkOp(); 
                }
            }
        }
    );

    if ( counter % 1000 > 0 )
        outputBulk.execute();


    // print the results
    outputColl.find({}).sort({count: -1}).forEach(printjson); 
    
    var end = Date.now();
    var duration = (end - start)/1000;
    printjson("Duration: " + duration + " seconds");

    printjson(" | DONE | ");
}

gatherStats();
```

Alternatively move data to memory:

```js 
    var statsDict = {}; // or better Object.create(null);    
    statsColl.find({}).forEach( function(doc) { statsDict[doc._id] = doc.count } );
    
    // could also use: var statsArray = statsCursor.toArray();
    
    inputCursor.forEach( function(doc) {
        if (doc.address in statsDict)
        { 
            doc["count"] = statsDict[doc.address]; 
            outputBulk.insert(doc); 
        }
    });
    outputBulk.execute();
```