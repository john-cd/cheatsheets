---
title: ElasticSearch Architecture and Configuration
category: search
tags: elasticsearch
---

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
