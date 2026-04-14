---
title: ElasticSearch APIs
category: search
tags: elasticsearch
---

## ElasticSearch 8.x Modern APIs

With version 8.0, security is enabled by default.

### Basic Indexing (cURL)
```shell
curl -X POST "https://localhost:9200/my-index-000001/_doc/" -u elastic:password -H 'Content-Type: application/json' -d'
{
  "@timestamp": "2099-11-15T13:12:00",
  "message": "GET /search HTTP/1.1 200 1070000",
  "user": {
    "id": "kimchy"
  }
}
' --insecure
```

### Search API
```shell
curl -X GET "https://localhost:9200/my-index-000001/_search?pretty" -u elastic:password -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  }
}
' --insecure
```

### Python Client Example
```python
from elasticsearch import Elasticsearch

# Create the client instance
client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "password"),
    verify_certs=False
)

# Successful response!
client.info()
```
