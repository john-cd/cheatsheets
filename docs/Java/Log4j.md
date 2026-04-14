---
title: Log4j2
category: java
tags: logging
---

# Log4j2

Apache Log4j2 is the modern upgrade to Log4j, providing significant improvements in performance (async loggers).

## Log4Shell Mitigation Context
**Important:** Versions of Log4j2 between 2.0-beta9 and 2.14.1 are vulnerable to Log4Shell (CVE-2021-44228).
**Fix:** Always ensure you are using Log4j2 version **2.17.1 or newer**.

## Dependencies
```xml
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-api</artifactId>
    <version>2.20.0</version>
</dependency>
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-core</artifactId>
    <version>2.20.0</version>
</dependency>
```

## log4j2.xml Configuration
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
  <Appenders>
    <Console name="Console" target="SYSTEM_OUT">
      <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
    </Console>
  </Appenders>
  <Loggers>
    <Root level="info">
      <AppenderRef ref="Console"/>
    </Root>
  </Loggers>
</Configuration>
```
