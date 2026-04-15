---
title: ElasticSearch Cheatsheet
category: search
tags: IR
---
# Cheatsheets

[Jolicode](https://elasticsearch-cheatsheet.jolicode.com/)

## Development URLs

[Kibana (port 5601)](https://localhost:5601)

[Sense](https://localhost:5601/app/sense)

[ElasticSearch (port 9200)](https://localhost:9200)

## CURL

```bash
curl -X<VERB> '<PROTOCOL>://<HOST>:<PORT>/<PATH>?<QUERY_STRING>' -d '<BODY>'
```

Verb is GET, POST, PUT, HEAD, or DELETE.

### Examples

```bash
curl -XGET 'https://localhost:9200/_count?pretty' -d '{ "query": { "match_all": {} }}'
```

```bash
curl -XGET <id>.us-west-2.es.amazonaws.com

curl -XGET 'https://<id>.us-west-2.es.amazonaws.com/_count?pretty' -d '{ "query": { "match_all": {} } }'

curl -XPUT https://<id>.us-west-2.es.amazonaws.com/movies/movie/tt0116996 -d '{"directors" : ["Tim Burton"],"genres" : ["Comedy","Sci-Fi"], "plot": "The Earth is invaded by Martians with irresistible weapons and a cruel sense of humor.", "title" : "Mars Attacks!", "actors" :["Jack Nicholson","Pierce Brosnan","Sarah Jessica Parker"], "year" : 1996}'
```

## Sense

Sense syntax is similar to curl:

Index a document

```txt
PUT index/type/1
{
 "body": "here"
}
```

and retrieve it

```txt
GET index/type/1
```

## PLUGINS

### **URL pattern**

`https://yournode:9200/_plugin/<plugin name>`

On Debian, the script is in: `/usr/share/elasticsearch/bin/plugin`.

### **Install various plugins**

```bash
./bin/plugin --install mobz/elasticsearch-head
./bin/plugin --install lmenezes/elasticsearch-kopf/1.2
./bin/plugin --install elasticsearch/marvel/latest
```

### **Remove a plugin**

```bash
./bin/plugin --remove
```

### **List installed plugins**

```bash
./bin/plugin --list
```

```txt
GET /_nodes?plugin=true
```

[Elasticsearch monitoring and management plugins](https://blog.codecentric.de/en/2014/03/elasticsearch-monitoring-and-management-plugins/)

### **Head**

[Head](https://mobz.github.io/elasticsearch-head/)

1. `elasticsearch/bin/plugin -install mobz/elasticsearch-head`
2. open [https://localhost:9200/_plugin/head](https://localhost:9200/_plugin/head)

[elastichq.org](https://www.elastichq.org/)

### **BigDesk**

Live charts and statistics for elasticsearch cluster:
[BigDesk](https://bigdesk.org/)

### **Kopf**

[Kopf](https://github.com/lmenezes/elasticsearch-kopf)

```bash
./bin/plugin --install lmenezes/elasticsearch-kopf/1.2`
```

### **Marvel**

```bash
./bin/plugin --install elasticsearch/marvel/latest
```

## Integrations (CMS, import/export, hadoop...)

[Integrations](https://www.elastic.co/guide/en/elasticsearch/plugins/current/integrations.html)

### **Aspire**

[Aspire](https://www.searchtechnologies.com/aspire-for-elasticsearch)

Aspire is a framework and libraries of extensible components designed to enable creation of solutions to acquire data from one or more content repositories (such as file systems, relational databases, cloud storage, or content management systems), extract metadata and text from the documents, analyze, modify and enhance the content and metadata if needed, and then publish each document, together with its metadata, to a search engine or other target application

[Docs](https://wiki.searchtechnologies.com/index.php/Main_Page)

### **Integration with Hadoop**

[Integration with Hadoop](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/index.html)

[Bulk loading for elastic search https://infochimps.com](https://github.com/infochimps-labs/wonderdog)

### **Integration with Spring**

[Spring Data](https://github.com/spring-projects/spring-data-elasticsearch)

### **WordPress**

[Wordpress](https://github.com/wallmanderco/elasticsearch-indexer)

## TOOLS

BI platforms that can use ES as an analytics engine:

- Kibana
- [Grafana](https://grafana.org/)
- BIRT
  - [Birt](https://developer.actuate.com/community/forum/index.php?/topic/36913-birt-web-service-rest-json/?p=138062)
  - [Birt](https://developer.actuate.com/community/forum/index.php?/topic/36913-birt-web-service-rest-json/?p=138062)

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
- [scrutmydocs.org](https://www.scrutmydocs.org/)
- [qbox.io](https://qbox.io/blog/series/machine-learning)

## Java API

- [Java clients](https://www.elastic.co/blog/found-java-clients-for-elasticsearch)
- [elasticsearch tutorial](https://github.com/jaibeermalik/elasticsearch-tutorial)
- [elasticsearchfr/](https://github.com/elasticsearchfr/hands-on)
- [IBM](https://www.ibm.com/developerworks/library/j-use-elasticsearch-java-apps/index.html)
- [dzone](https://dzone.com/articles/elasticsearch-java-api)

## BASICS

An Elasticsearch cluster can contain multiple indices, which in turn contain multiple types. These types hold multiple documents, and each document has multiple fields.

## Explore (using Sense)

`GET _stats/`

\# List indices

```txt
GET /_cat/indices/
GET /_cat/indices/my_ind*
```

\# Get info about one index

```txt
GET /twitter
GET /my_index_nr_1*/_settings?pretty   or ?v
GET /twitter/_settings,_mappings
```

The available features are _settings,_mappings, _warmers and_aliases

\# cluster

```txt
GET /_nodes
```

\# insert data

```txt
PUT my_index/user/1
{
"first_name":    "John",
"last_name":     "Smith",
"date_of_birth": "1970-10-24"
}
```

\#search

```txt
GET my_index/_search

GET _count?pretty
```

\# Data schema

```txt
GET my_index/_mapping
```

## INSERT DOCUMENTS

```txt
PUT /index/type/ID
PUT /megacorp/employee/1
{ "first_name" : "John", "last_name" : "Smith", "age" : 25, "about" : "I love to go rock climbing", "interests": [ "sports", "music" ]}

PUT /megacorp/employee/2
{ "first_name" : "Jane", "last_name" : "Smith", "age" : 32, "about" : "I like to collect rock albums", "interests": [ "music" ]}

GET /megacorp/employee/1
```

Field names can be any valid string, but may not include periods.
Every document in Elasticsearch has a version number. Every time a change is made to a document (including deleting it), the _version number is incremented.

### *Optimistic concurrency control*

```txt
PUT /website/blog/1?version=1  { "title": "My first blog entry", "text": "Starting to get the hang of this..."}

We want this update to succeed only if the current _version of this document in our index is version 1

External version:

PUT /website/blog/2?version=5&version_type=external { "title": "My first external blog entry", "text": "Starting to get the hang of this..."}
```

## INSERT DOCUMENTS - AUTOGENERATED IDS

```txt
POST /website/blog/
{
"title": "My second blog entry",
"text":  "Still trying this out...",
"date":  "2014/01/01"
}
```

Response:

```txt
{
"_index":    "website",
"_type":     "blog",
"_id":       "AVFgSgVHUP18jI2wRx0w",
"_version":  1,
"created":   true
}
```

\#  creating an entirely new document and not overwriting an existing one

```txt
PUT /website/blog/123?op_type=create { ... }
PUT /website/blog/123/_create { ... }
```

## RETRIEVE DOCUMENTS

```txt
GET /website/blog/123 # Optional ?pretty.
```

  { "_index" : "website", "_type" : "blog", "_id" : "123", "_version" : 1, "found" : true, "_source" : { "title": "My first blog entry", "text": "Just trying this out...", "date": "2014/01/01" }}

\# Contains just the fields that we requested

```txt
GET /website/blog/123?_source=title,text
```

\# Just get the original doc

```txt
GET /website/blog/123/_source
```

\# check if doc exists -- HTTP 200 or 404

```bash
curl -i -XHEAD https://localhost:9200/website/blog/123
```

\# Note: HEAD/exists requests do not work in Sense
\# because they only return HTTP headers, not
\# a JSON body

\# multiple docs at once

```txt
GET /website/blog/_mget { "ids" : [ "2", "1" ]}
```

## UPDATE

Documents in Elasticsearch are immutable; we cannot change them. Instead, if we need to update an existing document, we reindex or replace it

\# Accepts a partial document as the doc parameter, which just gets merged with the existing document.

```txt
POST /website/blog/1/_update
{ "doc" : { "tags" : [ "testing" ], "views": 0 }}
```

\# Script

```txt
POST /website/blog/1/_update
{ "script" : "ctx._source.views+=1"}
```

\# script with parameters

```txt
POST /website/blog/1/_update
{ "script" : "ctx._source.tags+=new_tag", "params" : { "new_tag" : "search" }}
```

\# upsert

```txt
POST/website/pageviews/1/_update
{"script":"ctx._source.views+=1","upsert":{"views":1}}
```

## DELETE

```txt
DELETE /website/blog/123
```

\# delete doc based on its contents

```txt
POST /website/blog/1/_update { "script" : "ctx.op = ctx._source.views == count ? 'delete' : 'none'", "params" : { "count": 1 }}
```

## BULK

```txt
POST /_bulk
{"delete":{"_index":"website","_type":"blog","_id":"123"}}
{"create":{"_index":"website","_type":"blog","_id":"123"}} # Create a document only if the document does not already exist.
{"title":"My first blog post"}
{"index":{"_index":"website","_type":"blog"}}
{"title":"My second blog post"}
{"update":{"_index":"website","_type":"blog","_id":"123","_retry_on_conflict":3}}
{"doc":{"title":"My updated blog post"}}
```

Bulk in the same index or index/type

```txt
POST /website/_bulk
{"index":{"_type":"log"}}
{"event":"User logged in"}
{"index":{"_type":"blog"}}
{"title":"My second blog post"}
```

Try  around 5-15MB in size.

## MATCH

\# Find all employees who enjoy "rock" or "climbing"

```txt
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

```txt
{
"multi_match": {
  "query":    "full text search",
  "fields":  [ "title", "body" ]
}}
```

## MULTIPLE INDICES OR TYPES

```txt
    # All documents all indices.
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
```

## PAGINATION

```txt
GET /_search?size=5GET /_search?size=5&from=5
```

## SORTING

```txt
GET /_search { "query" : { "bool" : { "filter" : { "term" : { "user_id" : 1 }} } }, "sort": { "date": { "order": "desc" }}}
```

For string sorting, use multi-field mapping:

```txt
"tweet": { "type": "string", "analyzer": "english", "fields": { "raw": {"type": "string", "index": "not_analyzed" } }}
```

The main tweet field is just the same as before: an analyzed full-text field.
The new tweet.raw subfield is not_analyzed.

then sort on the new field

```txt
GET /_search { "query": { "match": { "tweet": "elasticsearch" } }, "sort": "tweet.raw"}
```

## HIGHLIGHTS

Find all employees who enjoy "rock climbing" - and highlight the matches

```txt
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
```

## ANALYSIS

An analyzer is really just a wrapper that combines three functions into a single package:

- Character filters
- Tokenizer
- Token filters

### See how text is analyzed

```txt
GET /_analyze { "analyzer": "standard", "text": "Text to analyze"}
```

### test analyzer

```txt
GET /gb/_analyze { "field": "tweet", "text": "Black-cats"}
```

## AGGREGATES

Aggregations and searches can span multiple indices

### Calculate the most popular interests for all employees

```txt
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
```

### Calculate the most popular interests for employees named "Smith"

```txt
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
```

### Calculate the average age of employee per interest - hierarchical aggregates

```txt
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
```

requires in config/elasticsearch.yml

- script.inline: true
- script.indexed: true

```txt
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
```

## INDEX MANAGEMENT

By default, indices are assigned five primary shards. The number of primary shards can be set only when an index is created and never changed

- Add an index

```txt
  PUT /blogs { "settings" : { "number_of_shards" : 3, "number_of_replicas" : 1 }}
  PUT /blogs/_settings { "number_of_replicas" : 2}
```

- ElasticSearch Shards should be 50 GB or less in size.
- Use aliases to shelter the underlying index (or indices) and allow index swapping

## CLUSTER MANAGEMENT

```txt
GET /_cluster/health
```

## CONFIGURATION

- config directory
- yaml file

- Sets the JVM heap size to 0.5 memory size. The OS will use it for file system cache
- Prefer not to allocate 30GB !! --> uncompressed pointers
- Never let the JVM swap    bootstrap.mlockall = true
- Keep the JVM defaults
- Do not use G1GC alternative garbage collector

```txt
cluster.name: <my cluster>
```

- All nodes in the cluster must have the same cluster name

```txt
node.name: <my_node_name>
```

```txt
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
