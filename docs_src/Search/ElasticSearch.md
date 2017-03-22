---
title: ElasticSearch Cheatsheet
category: search
tags: IR
---

## Cheatsheets

[Jolicode](http://elasticsearch-cheatsheet.jolicode.com/)


## Development URLs

[Kibana (port 5601)](http://localhost:5601)

[Sense](http://localhost:5601/app/sense)

[ElasticSearch (port 9200)](http://localhost:9200)


## INSTALL

1. Install [curl](http://curl.haxx.se/download.html)
2. Install [Java](http://www.java.com)
3. Download [ElasticSearch](https://www.elastic.co/downloads/elasticsearch)
4. Optionally change the `cluster.name` in the `elasticsearch.yml` configuration

```bash
cd elasticsearch-<version>
./bin/elasticsearch -d
# or on Windows 
# bin\elasticsearch.bat
curl 'http://localhost:9200/?pretty'
```

5.  Install [Kibana](https://www.elastic.co/downloads/kibana)
    * Open `config/kibana.yml` in an editor
    * Set the elasticsearch.url to point at your Elasticsearch instance
    * Run `./bin/kibana` (orbin\kibana.bat on Windows)
    * Point your browser at [http://localhost:5601](http://localhost:5601)

6. Install [Sense](https://www.elastic.co/guide/en/elasticsearch/guide/current/running-elasticsearch.html#sense)

```bash
./bin/kibana plugin --install elastic/sense
```

*On Windows:* 

```bash
bin\kibana.bat plugin --install elastic/sense
```  
Then go to

[http://localhost:5601/app/sense](http://localhost:5601/app/sense)


## CURL

```bash
curl -X<VERB> '<PROTOCOL>://<HOST>:<PORT>/<PATH>?<QUERY_STRING>' -d '<BODY>'
```
  
*verb is GET, POST, PUT, HEAD, or DELETE*

### Examples

```bash
curl -XGET 'http://localhost:9200/_count?pretty' -d '{ "query": { "match_all": {} }}'
```

```bash
curl -XGET <id>.us-west-2.es.amazonaws.com

curl -XGET 'https://<id>.us-west-2.es.amazonaws.com/_count?pretty' -d '{ "query": { "match_all": {} } }'

curl -XPUT https://<id>.us-west-2.es.amazonaws.com/movies/movie/tt0116996 -d '{"directors" : ["Tim Burton"],"genres" : ["Comedy","Sci-Fi"], "plot": "The Earth is invaded by Martians with irresistible weapons and a cruel sense of humor.", "title" : "Mars Attacks!", "actors" :["Jack Nicholson","Pierce Brosnan","Sarah Jessica Parker"], "year" : 1996}'
```

## Sense

Sense syntax is similar to curl:

Index a document

```
PUT index/type/1
{
 "body": "here"
}
```
and retrieve it

```
GET index/type/1
```

## PLUGINS

**URL pattern**

`http://yournode:9200/_plugin/<plugin name>`

On Debian, the script is in: `/usr/share/elasticsearch/bin/plugin`.

__Install various plugins__

```bash
./bin/plugin --install mobz/elasticsearch-head
./bin/plugin --install lmenezes/elasticsearch-kopf/1.2
./bin/plugin --install elasticsearch/marvel/latest
```
__Remove a plugin__

```bash
./bin/plugin --remove
```

__List installed plugins__

```bash
./bin/plugin --list
```
```
GET /_nodes?plugin=true
```
[Elasticsearch monitoring and management plugins](https://blog.codecentric.de/en/2014/03/elasticsearch-monitoring-and-management-plugins/)

**Head**

[Head](http://mobz.github.io/elasticsearch-head/)

1. `elasticsearch/bin/plugin -install mobz/elasticsearch-head`
2. open [http://localhost:9200/_plugin/head](http://localhost:9200/_plugin/head)

[elastichq.org](http://www.elastichq.org/)

**BigDesk**

Live charts and statistics for elasticsearch cluster: 
[BigDesk](http://bigdesk.org/)

**Kopf**

[Kopf](https://github.com/lmenezes/elasticsearch-kopf)

```
./bin/plugin --install lmenezes/elasticsearch-kopf/1.2`
```

**Marvel**

```bash
./bin/plugin --install elasticsearch/marvel/latest
```

## Integrations (CMS, import/export, hadoop...)

[Integrations](https://www.elastic.co/guide/en/elasticsearch/plugins/current/integrations.html)

**Aspire**

[Aspire](http://www.searchtechnologies.com/aspire-for-elasticsearch)

Aspire is a framework and libraries of extensible components designed to enable creation of solutions to acquire data from one or more content repositories (such as file systems, relational databases, cloud storage, or content management systems), extract metadata and text from the documents, analyze, modify and enhance the content and metadata if needed, and then publish each document, together with its metadata, to a search engine or other target application

[Docs](https://wiki.searchtechnologies.com/index.php/Main_Page)

**Integration with Hadoop**

[Integration with Hadoop](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/index.html)

[Bulk loading for elastic search http://infochimps.com](https://github.com/infochimps-labs/wonderdog)

**Integration with Spring**

[Spring Data](https://github.com/spring-projects/spring-data-elasticsearch)

**WordPress**

[Wordpress](https://github.com/wallmanderco/elasticsearch-indexer)

## TOOLS

BI platforms that can use ES as an analytics engine:

- Kibana
- [Grafana](grafana.org/)
- BIRT
    * [Birt](http://developer.actuate.com/community/forum/index.php?/topic/36913-birt-web-service-rest-json/?p=138062)
    * [Birt](http://developer.actuate.com/community/forum/index.php?/topic/36913-birt-web-service-rest-json/?p=138062)


- Adminer
    - [Adminer.org](https://www.adminer.org/)
    - Database management in a single PHP file. Works with MySQL, PostgreSQL, SQLite, MS SQL, Oracle, SimpleDB, Elasticsearch, MongoDB. Needs a webserver + PHP: [WAMP](https://bitnami.com/stack/wamp)

- Mongolastic
    - A tool that migrates data from MongoDB to Elasticsearch and vice versa
    - [Mongolastic](https://github.com/ozlerhakan/mongolastic)

- Elasticsearch-exporter
    - [Elasticsearch-exporter](https://github.com/mallocator/Elasticsearch-Exporter)

## Code Examples - developing a Web UI for ES

- [Sitepoint](https://www.sitepoint.com/building-recipe-search-site-angular-elasticsearch/)
- [CottageLabs](https://github.com/CottageLabs/facetview2)
- [scrutmydocs.org](http://www.scrutmydocs.org/)
- [qbox.io](https://qbox.io/blog/series/machine-learning)

## Java API

- [Java clients](https://www.elastic.co/blog/found-java-clients-for-elasticsearch)
- [elasticsearch tutorial](https://github.com/jaibeermalik/elasticsearch-tutorial)
- [elasticsearchfr/](https://github.com/elasticsearchfr/hands-on)
- [IBM](http://www.ibm.com/developerworks/library/j-use-elasticsearch-java-apps/index.html)
- [dzone](https://dzone.com/articles/elasticsearch-java-api)


# BASICS

An Elasticsearch cluster can contain multiple indices, which in turn contain multiple types. These types hold multiple documents, and each document has multiple fields.


## Explore (using Sense)

`GET _stats/`

\# List indices

```
GET /_cat/indices/
GET /_cat/indices/my_ind*
```

\# Get info about one index

```
GET /twitter
GET /my_index_nr_1*/_settings?pretty   or ?v
GET /twitter/_settings,_mappings
```

The available features are _settings, _mappings, _warmers and _aliases

\# cluster

```
GET /_nodes
```

\# insert data

```
PUT my_index/user/1
{
"first_name":    "John",
"last_name":     "Smith",
"date_of_birth": "1970-10-24"
}
```

\#search

```
GET my_index/_search

GET _count?pretty
```

\# Data schema

```
GET my_index/_mapping
```



## INSERT DOCUMENTS

```
PUT /index/type/ID
PUT /megacorp/employee/1
{ "first_name" : "John", "last_name" : "Smith", "age" : 25, "about" : "I love to go rock climbing", "interests": [ "sports", "music" ]}

PUT /megacorp/employee/2
{ "first_name" : "Jane", "last_name" : "Smith", "age" : 32, "about" : "I like to collect rock albums", "interests": [ "music" ]}

GET /megacorp/employee/1
```

Field names can be any valid string, but may not include periods.
Every document in Elasticsearch has a version number. Every time a change is made to a document (including deleting it), the _version number is incremented.

*Optimistic concurrency control*

```
PUT /website/blog/1?version=1  { "title": "My first blog entry", "text": "Starting to get the hang of this..."}

We want this update to succeed only if the current _version of this document in our index is version 1

External version:

PUT /website/blog/2?version=5&version_type=external { "title": "My first external blog entry", "text": "Starting to get the hang of this..."}
```

## INSERT DOCUMENTS - AUTOGENERATED IDS

```
POST /website/blog/
{
"title": "My second blog entry",
"text":  "Still trying this out...",
"date":  "2014/01/01"
}
```  

Response:
```
{
"_index":    "website",
"_type":     "blog",
"_id":       "AVFgSgVHUP18jI2wRx0w",
"_version":  1,
"created":   true
}
```

\#  creating an entirely new document and not overwriting an existing one

```
PUT /website/blog/123?op_type=create { ... }
PUT /website/blog/123/_create { ... }
```

## RETRIEVE DOCUMENTS

```
GET /website/blog/123  # optional ?pretty
```
  { "_index" : "website", "_type" : "blog", "_id" : "123", "_version" : 1, "found" : true, "_source" : { "title": "My first blog entry", "text": "Just trying this out...", "date": "2014/01/01" }}

\# Contains just the fields that we requested

```
GET /website/blog/123?_source=title,text
```

\# Just get the original doc

```
GET /website/blog/123/_source
```

\# check if doc exists -- HTTP 200 or 404

```bash
curl -i -XHEAD http://localhost:9200/website/blog/123
```

\# Note: HEAD/exists requests do not work in Sense
\# because they only return HTTP headers, not
\# a JSON body

\# multiple docs at once

```
GET /website/blog/_mget { "ids" : [ "2", "1" ]}
```

## UPDATE

Documents in Elasticsearch are immutable; we cannot change them. Instead, if we need to update an existing document, we reindex or replace it

\# Accepts a partial document as the doc parameter, which just gets merged with the existing document.

```
POST /website/blog/1/_update
{ "doc" : { "tags" : [ "testing" ], "views": 0 }}
```

\# Script
 
``` 
POST /website/blog/1/_update
{ "script" : "ctx._source.views+=1"}
```

\# script with parameters

```
POST /website/blog/1/_update
{ "script" : "ctx._source.tags+=new_tag", "params" : { "new_tag" : "search" }}
```

\# upsert

```
POST/website/pageviews/1/_update
{"script":"ctx._source.views+=1","upsert":{"views":1}}
```

## DELETE

```
DELETE /website/blog/123
```

\# delete doc based on its contents

```
POST /website/blog/1/_update { "script" : "ctx.op = ctx._source.views == count ? 'delete' : 'none'", "params" : { "count": 1 }}
```

## BULK

```
POST /_bulk
{"delete":{"_index":"website","_type":"blog","_id":"123"}}
{"create":{"_index":"website","_type":"blog","_id":"123"}} #  Create a document only if the document does not already exist
{"title":"My first blog post"}
{"index":{"_index":"website","_type":"blog"}}
{"title":"My second blog post"}
{"update":{"_index":"website","_type":"blog","_id":"123","_retry_on_conflict":3}}
{"doc":{"title":"My updated blog post"}}
```

Bulk in the same index or index/type

```
POST /website/_bulk
{"index":{"_type":"log"}}
{"event":"User logged in"}
{"index":{"_type":"blog"}}
{"title":"My second blog post"}
```

Try  around 5-15MB in size.


## SEARCH

Every field in a document is indexed and can be queried.

\# Search for all employees in the megacorp index:

```
GET /megacorp/employee/_search
```

\# Search for all employees in the megacorp index
\# who have "Smith" in the last_name field

```
GET /megacorp/employee/_search?q=last_name:Smith
```

\# Same query as above, but using the Query DSL

```
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

```
GET /_all/tweet/_search?q=tweet:elasticsearch
```

Don't forget to URL encode special characters e.g. +name:john +tweet:mary

```
GET /_search?q=%2Bname%3Ajohn+%2Btweet%3Amary
```

The + prefix indicates conditions that must be satisfied for our query to match. Similarly a - prefix would indicate conditions that must not match. All conditions without a + or - are optional

```
+name:(mary john) +date:>2014-09-10 +(aggregations geo) # last part searches _all
```

## QUERY DSL

When used in filtering context, the query is said to be a "non-scoring" or "filtering" query. That is, the query simply asks the question: "Does this document match?". The answer is always a simple, binary yes|no.
When used in a querying context, the query becomes a "scoring" query.

```
# Find all employees whose `last_name` is Smith
# and who are older than 30
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

## MATCH

\# Find all employees who enjoy "rock" or "climbing"

```
GET /megacorp/employee/_search
{
"query" : {
  "match" : {
      "about" : "rock climbing"
  }
}
}
```

The match query should be the standard query that you reach for whenever you want to query for a full-text or exact value in almost any field.
If you run a match query against a full-text field, it will analyze the query string by using the correct analyzer for that field before executing the search
If you use it on a field containing an exact value, such as a number, a date, a Boolean, or a not_analyzedstring field, then it will search for that exact value

## MATCH ON MULTIPLE FIELDS

```
{
"multi_match": {
  "query":    "full text search",
  "fields":  [ "title", "body" ]
}}
```

## EXACT SEARCH

\# Find all employees who enjoy "rock climbing"

```
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

```
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


## MULTIPLE INDICES OR TYPES

    # all documents all indices
  /_search

  /gb,us/_search
  Search all types in the gb and us indices

  /g*,u*/_search
  Search all types in any indices beginning with g or beginning with u

  /gb/user/_search
  Search type user in the gb index

  /gb,us/user,tweet/_search
  Search types user and tweet in the gb and us indices

  /_all/user,tweet/_search
  Search types user and tweet in all indices


## PAGINATION

     GET /_search?size=5GET /_search?size=5&from=5

## SORTING

     GET /_search { "query" : { "bool" : { "filter" : { "term" : { "user_id" : 1 }} } }, "sort": { "date": { "order": "desc" }}}

For string sorting, use multi-field mapping:

     "tweet": { "type": "string", "analyzer": "english", "fields": { "raw": {"type": "string", "index": "not_analyzed" } }}

The main tweet field is just the same as before: an analyzed full-text field.
The new tweet.raw subfield is not_analyzed.

then sort on the new field

     GET /_search { "query": { "match": { "tweet": "elasticsearch" } }, "sort": "tweet.raw"}


## HIGHLIGHTS

\# Find all employees who enjoy "rock climbing" - highlights
\# and highlight the matches

  GET /megacorp/employee/_search
  {
      "query" : {
          "match_phrase" : {
              "about" : "rock climbing"
          }
      },
      "highlight": {
          "fields" : {
              "about" : {}
          }
      }
  }


## ANALYSIS

An analyzer is really just a wrapper that combines three functions into a single package:

    * Character filters
    * Tokenizer
    * Token filters

\#  See how text is analyzed

  GET /_analyze { "analyzer": "standard", "text": "Text to analyze"}

\# test analyzer

  GET /gb/_analyze { "field": "tweet", "text": "Black-cats"}


## MAPPINGS (schemas)

Every type has its own mapping, or schema definition. A mapping defines the fields within a type, the datatype for each field, and how the field should be handled by Elasticsearch. A mapping is also used to configure metadata associated with the type.

You can control dynamic nature of mappings

Mapping (or schema definition) for the tweet type in the gb index

```
  GET /gb/_mapping/tweet
```

Elasticsearch supports the following simple field types:
* String: string
* Whole number: byte, short, integer, long
* Floating-point: float, double
* Boolean: boolean
* Date: date

Fields of type string are, by default, considered to contain full text. That is, their value will be passed through an analyzer before being indexed, and a full-text query on the field will pass the query string through an analyzer before searching.
The two most important mapping attributes for string fields are index and analyzer.

The index attribute controls how the string will be indexed. It can contain one of three values:
* analyzed  First analyze the string and then index it. In other words, index this field as full text.
* not_analyzed  Index this field, so it is searchable, but index the value exactly as specified. Do not analyze it.
* no  Don’t index this field at all. This field will not be searchable.

If we want to map the field as an exact value, we need to set it to not_analyzed:
```
  {
    "tag": {
    "type": "string",
    "index": "not_analyzed"
    }
  }
```

For analyzed string fields, use the analyzer attribute to specify which analyzer to apply both at search time and at index time. By default, Elasticsearch uses the standard analyzer, but you can change this by specifying one of the built-in analyzers, such as whitespace, simple, or english:
```
  {
    "tweet": {
    "type": "string",
    "analyzer": "english"
    }
  }
```

\#  create a new index, specifying that the tweet field should use the english analyzer

PUT /gb
  { "mappings":
       { "tweet" :
                 { "properties" : {
                      "tweet" : { "type" : "string", "analyzer": "english" },
                      "date" : { "type" : "date" },
                      "name" : { "type" : "string" },
                      "user_id" : { "type" : "long" }
                    }}}}

null, arrays, objects: see [complex core fields](https://www.elastic.co/guide/en/elasticsearch/guide/current/complex-core-fields.html)


## AGGREGATES

Aggregations and searches can span multiple indices

\# Calculate the most popular interests for all employees

  GET /megacorp/employee/_search
  {
    "aggs": {
      "all_interests": {
        "terms": {
          "field": "interests"
        }
      }
    }
  }

\# Calculate the most popular interests for
\# employees named "Smith"

  GET /megacorp/employee/_search
  {
    "query": {
      "match": {
        "last_name": "smith"
      }
    },
    "aggs": {
      "all_interests": {
        "terms": {
          "field": "interests"
        }
      }
    }
  }

\# Calculate the average age of employee per interest - hierarchical aggregates

  GET /megacorp/employee/_search
  {
      "aggs" : {
          "all_interests" : {
              "terms" : { "field" : "interests" },
              "aggs" : {
                  "avg_age" : {
                      "avg" : { "field" : "age" }
                  }
              }
          }
      }
  }

\# requires in config/elasticsearch.yml
\# script.inline: true
\# script.indexed: true

  GET /tlo/contacts/_search
  {
    "size" : 0,
    "query": {
      "constant_score": {
        "filter": {
          "terms": {
            "version": [
              "20160301",
              "20160401"
            ]
          }
        }
      }
    },
    "aggs": {
      "counts": {
        "cardinality": {
          "script": "doc['first_name'].value + ' ' + doc['last_name'].value + ' ' + doc['company'].value",
          "missing": "N/A"
        }
      }
    }
  }


## INDEX MANAGEMENT

By default, indices are assigned five primary shards. The number of primary shards can be set only when an index is created and never changed

\# Add an index

```
  PUT /blogs { "settings" : { "number_of_shards" : 3, "number_of_replicas" : 1 }}
  PUT /blogs/_settings { "number_of_replicas" : 2}
```

- ElasticSearch Shards should be 50 GB or less in size.
- Use aliases to shelter the underlying index (or indices) and allow index swapping


## CLUSTER MANAGEMENT

     GET /_cluster/health

## CONFIGURATION

- config directory
- yaml file

- Sets the JVM heap size to 0.5 memory size. The OS will use it for file system cache
- Prefer not to allocate 30GB !! --> uncompressed pointers
- Never let the JVM swap    bootstrap.mlockall = true
- Keep the JVM defaults
- Do not use G1GC alternative garbage collector

```
cluster.name: <my cluster>
```

- All nodes in the cluster must have the same cluster name

```
node.name: <my_node_name>
```
```
./bin/elasticsearch --node.name=`hostname`
```
to override the configuration file

- HTTP port: 9200 and successors
- Transport : 9300 (internal communications)

### Discovery

- AWS plugin available   --> also include integration with S3 (snapshot to S3)
- AWS: multi-AZ is OK but replication across far data centers is not recommended
- See: resiliency

Sites plugins -- kopf / head / paramedic / bigdesk / kibana
- contain static web content (JS, HTML....)

Install plugins on ALL machines of the cluster

To install,

```bash
  ./bin/plugin install marvel-agent
  ./bin/plugin remove marvel-agent
```
One type per index is recommended, except for parent child / nested indexes.

index size optimization:
- can disable `_source` and `_all` (the index that captures every field - not needed unless the top search bar changes)
- by default, Kibana will search `_all`

data types:
string, number, bool, datetime, binary, array, object, geo_point, geo_shape, ip, multifield
binary should be base64 encoded before storage


### MAINTENANCE

Steps to restore elastic search data:

1. Stop elastic search
2. Extract the zip file (dump file)
3. Start elastic search
4. Reload elastic search

The commands to do the above are as below:

1. `systemctl stop elasticsearch`
2. extract gz file to destination path
3. `systemctl start elasticsearch`
4. `systemctl daemon-reload elasticsearch`


