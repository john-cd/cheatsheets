---
title: Logstash
category: search
tags: logstash
---

# Logstash

## Latest ELK Stack Configuration

Logstash 8.x pipeline example.

```conf
input {
  beats {
    port => 5044
  }
}

filter {
  grok {
    match => { "message" => "%{COMBINEDAPACHELOG}" }
  }
  date {
    match => [ "timestamp" , "dd/MMM/yyyy:HH:mm:ss Z" ]
  }
}

output {
  elasticsearch {
    hosts => ["https://localhost:9200"]
    user => "elastic"
    password => "changeme"
    ssl_certificate_verification => false
  }
  stdout { codec => rubydebug }
}
```
