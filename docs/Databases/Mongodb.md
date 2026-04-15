---
title: MongoDB Cheatsheet
category: databases
tags: NoSQL
comments: true
---

# MongoDB Cheatsheet

MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program (as opposed to [SQL](SQL.md)), MongoDB uses JSON-like documents with optional schemas.

## Import from CSV

The following command imports a CSV file into a MongoDB collection using the `mongoimport` tool.

```bash
mongoimport --db users --collection contacts --type csv --headerline --file contacts.csv
```

Specifying `--headerline` instructs mongoimport to determine the name of the fields using the first line in the CSV file.
Use the `--ignoreBlanks` option to ignore blank fields. For CSV and TSV imports, this option provides the desired functionality in most cases, because it avoids inserting fields with null values into your collection.

[MongoImport documentation](https://www.mongodb.com/docs/database-tools/mongoimport/)

## Print from a Cursor

```js
myCursor.forEach(console.log);

// Or.
while (myCollection.hasNext()) {
   console.log(myCollection.next());
}
```

## Aggregation Tips

```js
// Lowercase a string.
{ $project: { "address": { $toLower: "$address" } } },

// Extract field within embedded document.
{ $project: { "experience.location": 1 } },

// Flatten.
{ $unwind: "$experience"},
{ $group: { _id: "$_id", locs: { $push: { $ifNull: [ "$experience.location", "undefined" ] } } } }

// Output a collection.
{ $out: "myCollection2" }

// Get unique values.
{ $group: { _id: "$fulladdress" } }
```

## Make a Copy

Don't use copyTo - it is fully blocking... and deprecated in 3.x

- Use the Aggregation framework:

```js
db = db.getSiblingDB("myDB"); // Set current db for $out.
var myCollection = db.getCollection("myCollection");

// Project if needed, get uniques if needed, create a new collection.
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
--8<-- "docs/includes/gatherStats.js"
```

Alternatively move data to memory:

```js
    var statsDict = {}; // Or better Object.create(null).
    statsColl.find({}).forEach( function(doc) { statsDict[doc._id] = doc.count } );

    // Could also use: var statsArray = statsCursor.toArray().

    inputCursor.forEach( function(doc) {
        if (doc.address in statsDict)
        {
            doc["count"] = statsDict[doc.address];
            outputBulk.insert(doc);
        }
    });
    outputBulk.execute();
```
