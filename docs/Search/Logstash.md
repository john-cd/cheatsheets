# LogStash

## Operations

`logstash -w 4` to set the number of worker threads

Use `path.data` to distribute the data on multiple (EBS) disks

## Outputs

- MongoDB
- PagerDuty
- Nagios
- Graphite
- Ganglia
- StatsD
- Redis
- RabbitMQ

```txt
output {
     elasticsearch { }   # https://localhost:9200
}
```

```txt
output {
     redis {
          host => "redis.example.com"
          data_type =>: "list"

     }
}
```

### Output to file

```txt
output {
      file {

     }
}
```

## Filtering

Use "date" for normalizing dates:

```txt
filter {
     date{
         timezone => "America/Los_Angeles"
         locale => "en"      # English

     }
     geoip {

         source => "clientip"   # will read from clientip field
          database =>  ... # use MaxMind's GeoLiteCity by default
     }
     useragent {

     }
}
```

### Mutate a field

```txt
filter {
     if [action] == "login {
          mutate { remove_field => "secret" }
     }
}
```

### Conditionals both in `filter` and `outputs`

```txt
regexp
=~
!~
```

```txt
output {
     if [loglevel] == "ERROR"

}
```

## Interesting Plugins

[Stanford NLP library logstash plugin](https://github.com/jwconway/logstash-filter-stanford-nlp)

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
