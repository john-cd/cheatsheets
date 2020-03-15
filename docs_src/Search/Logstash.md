# LogStash

## Operations

``logstash -w 4`` to set the number of worker threads

Use ``path.data`` to distribute the data on multiple (EBS) disks


## Outputs

- MongoDB
- PagerDuty
- Nagios
- Graphite  
- Ganglia 
- StatsD
- Redis
- RabbitMQ

```
output {
     elasticsearch { }   # http://localhost:9200
}
```

```
output {
     redis {
          host => "redis.example.com"
          data_type =>: "list" 
          
     }
}
```

### Output to file

```
output {
      file { 

     }
}
```

## Filtering

Use "date" for normalizing dates:

```
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

```
filter { 
     if [action] == "login { 
          mutate { remove_field => "secret" }
     }
}
```

### Conditionals both in ``filter`` and ``outputs``

```
regexp 
=~  
!~
```

```
output { 
     if [loglevel] == "ERROR" 

}
```

## Interesting Plugins

[Stanford NLP library logstash plugin]( 
https://github.com/jwconway/logstash-filter-stanford-nlp
)

