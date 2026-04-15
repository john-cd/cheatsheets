---
title: ElasticSearch Setup
category: search
---

# ElasticSearch Setup

## INSTALL

1. Install [curl](https://curl.haxx.se/download.html)
2. Install [Java](https://www.java.com)
3. Download [ElasticSearch](https://www.elastic.co/downloads/elasticsearch)
4. Optionally change the `cluster.name` in the `elasticsearch.yml` configuration

```bash
cd elasticsearch-<version>
./bin/elasticsearch -d
# Or on Windows.
# Bin\elasticsearch.bat.
curl 'https://localhost:9200/?pretty'
```

1. Install [Kibana](https://www.elastic.co/downloads/kibana)

   - Open `config/kibana.yml` in an editor
   - Set the elasticsearch.url to point at your Elasticsearch instance
   - Run `./bin/kibana` (orbin\\kibana.bat on Windows)
   - Point your browser at [https://localhost:5601](https://localhost:5601)

2. Install [Sense](https://www.elastic.co/guide/en/elasticsearch/guide/current/running-elasticsearch.html#sense)

```bash
./bin/kibana plugin --install elastic/sense
```

*On Windows:*

```bash
bin\kibana.bat plugin --install elastic/sense
```

Then go to

[https://localhost:5601/app/sense](https://localhost:5601/app/sense)

## CLUSTER MANAGEMENT

```txt
GET /_cluster/health
```

## ELK Stack

[The Complete Guide to the ELK Stack - Logz.io](https://logz.io/learn/complete-guide-elk-stack/)
