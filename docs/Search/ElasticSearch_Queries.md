---
title: ElasticSearch Queries
category: search
---



# ElasticSearch Queries

## SEARCH

Every field in a document is indexed and can be queried.

\# Search for all employees in the megacorp index:

```txt
GET /megacorp/employee/_search
```

\# Search for all employees in the megacorp index
\# who have "Smith" in the last_name field

```txt
GET /megacorp/employee/_search?q=last_name:Smith
```

\# Same query as above, but using the Query DSL

```txt
GET /megacorp/employee/_search
{
    "query": {
      "match": {
        "last_name": "smith"
      }
    }
}
```

\# SEARCH QUERY STRING

```txt
GET /_all/tweet/_search?q=tweet:elasticsearch
```

Don't forget to URL encode special characters e.g. +name:john +tweet:mary

```txt
GET /_search?q=%2Bname%3Ajohn+%2Btweet%3Amary
```

The + prefix indicates conditions that must be satisfied for our query to match. Similarly a - prefix would indicate conditions that must not match. All conditions without a + or - are optional

```txt
+name:(mary john) +date:>2014-09-10 +(aggregations geo) # Last part searches _all.
```

## QUERY DSL

When used in filtering context, the query is said to be a "non-scoring" or "filtering" query. That is, the query simply asks the question: "Does this document match?". The answer is always a simple, binary yes|no.
When used in a querying context, the query becomes a "scoring" query.

```txt
# Find all employees whose `last_name` is Smith.
# And who are older than 30.
GET /megacorp/employee/_search
{
"query" : {
  "filtered" : {
      "filter" : {
      "range" : {
          "age" : { "gt" : 30 }
      }
      },
      "query" : {
      "match" : {
          "last_name" : "smith"
      }
      }
  }
}
}
```

## EXACT SEARCH

\# Find all employees who enjoy "rock climbing"

```txt
GET /megacorp/employee/_search
{
"query" : {
  "match_phrase" : {
      "about" : "rock climbing"
  }
}
}
```

\# EXACT VALUES

The term query is used to search by exact values, be they numbers, dates, Booleans, or not_analyzed exact-value string fields

The terms query is the same as the term query, but allows you to specify multiple values to match. If the field contains any of the specified values, the document matches

```txt
{ "terms": { "tag": [ "search", "full_text", "nosql" ] }}
```

\# Compound Queries

  {
     "bool": {
       "must": { "match": { "tweet": "elasticsearch" }},
        "must_not": { "match": { "name": "mary" }},
        "should": { "match": { "tweet": "full text" }},
        "filter": { "range": { "age" : { "gt" : 30 }} }
     }
  }

\# VALIDATE A QUERY

  GET /gb/tweet/_validate/query?explain { "query": { "tweet" : { "match" : "really powerful" } }}

\# understand why one particular document matched or, more important, why it didn’t match

  GET /us/tweet/12/_explain { "query" : { "bool" : { "filter" : { "term" : { "user_id" : 2 }}, "must" : { "match" : { "tweet" : "honeymoon" }} } }}

## MAPPINGS (schemas)

Every type has its own mapping, or schema definition. A mapping defines the fields within a type, the datatype for each field, and how the field should be handled by Elasticsearch. A mapping is also used to configure metadata associated with the type.

You can control dynamic nature of mappings

Mapping (or schema definition) for the tweet type in the gb index

```txt
  GET /gb/_mapping/tweet
```

Elasticsearch supports the following simple field types:

- String: string
- Whole number: byte, short, integer, long
- Floating-point: float, double
- Boolean: boolean
- Date: date

Fields of type string are, by default, considered to contain full text. That is, their value will be passed through an analyzer before being indexed, and a full-text query on the field will pass the query string through an analyzer before searching.
The two most important mapping attributes for string fields are index and analyzer.

The index attribute controls how the string will be indexed. It can contain one of three values:

- `analyzed`: First analyze the string and then index it. In other words, index this field as full text.
- `not_analyzed`: Index this field, so it is searchable, but index the value exactly as specified. Do not analyze it.
- `no`: Don’t index this field at all. This field will not be searchable.

If we want to map the field as an exact value, we need to set it to not_analyzed:

```txt
  {
    "tag": {
    "type": "string",
    "index": "not_analyzed"
    }
  }
```

For analyzed string fields, use the analyzer attribute to specify which analyzer to apply both at search time and at index time. By default, Elasticsearch uses the standard analyzer, but you can change this by specifying one of the built-in analyzers, such as whitespace, simple, or english:

```txt
  {
    "tweet": {
    "type": "string",
    "analyzer": "english"
    }
  }
```

### Create a new index, specifying that the tweet field should use the english analyzer

```txt
PUT /gb
  { "mappings":
       { "tweet" :
                 { "properties" : {
                      "tweet" : { "type" : "string", "analyzer": "english" },
                      "date" : { "type" : "date" },
                      "name" : { "type" : "string" },
                      "user_id" : { "type" : "long" }
                    }}}}
```

null, arrays, objects: see [complex core fields](https://www.elastic.co/guide/en/elasticsearch/guide/current/complex-core-fields.html)

## [Parent Child Relationships](https://qbox.io/blog/parent-child-relationships-in-elasticsearch)

```JSON
DELETE /test_index

PUT /test_index
{
   "mappings": {
      "parent_type": {
         "properties": {
            "num_prop": {
               "type": "integer"
            },
            "str_prop": {
               "type": "string"
            }
         }
      },
      "child_type": {
         "_parent": {
            "type": "parent_type"
         },
         "properties": {
            "child_num": {
               "type": "integer"
            },
            "child_str": {
               "type": "string"
            }
         }
      }
   }
}

POST /test_index/_bulk
{"index":{"_type":"parent_type","_id":1}}
{"num_prop":1,"str_prop":"hello"}
{"index":{"_type":"child_type","_id":1,"_parent":1}}
{"child_num":11,"child_str":"foo"}
{"index":{"_type":"child_type","_id":2,"_parent":1}}
{"child_num":12,"child_str":"bar"}
{"index":{"_type":"parent_type","_id":2}}
{"num_prop":2,"str_prop":"goodbye"}
{"index":{"_type":"child_type","_id":3,"_parent":2}}
{"child_num":21,"child_str":"baz"}

POST /test_index/child_type/_search

POST /test_index/child_type/2?parent=1
{
   "child_num": 13,
   "child_str": "bars"
}

POST /test_index/child_type/_search

POST /test_index/child_type/3/_update?parent=2
{
   "script": "ctx._source.child_num+=1"
}

POST /test_index/child_type/_search

POST /test_index/child_type/_search
{
    "query": {
        "term": {
           "child_str": {
              "value": "foo"
           }
        }
    }
}

POST /test_index/parent_type/_search
{
   "query": {
      "filtered": {
         "query": {
            "match_all": {}
         },
         "filter": {
            "has_child": {
               "type": "child_type",
               "filter": {
                  "term": {
                     "child_str": "foo"
                  }
               }
            }
         }
      }
   }
}
```
