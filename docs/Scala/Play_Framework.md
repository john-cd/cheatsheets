---
title: Play Framework
category: Scala
tag: Scala Akka Play Web REST
---

## Links

[Play Framework Documentation](https://www.playframework.com/documentation/3.0.x/Home)

Play 3.0 uses Apache Pekko instead of Akka.

## The Play application layout

The layout of a Play application is standardized to keep things as simple as possible.

```txt
app                      → Application sources
 └ assets                → Compiled asset sources
    └ stylesheets        → Typically LESS CSS sources
    └ javascripts        → Typically CoffeeScript sources
 └ controllers           → Application controllers
 └ models                → Application business layer
 └ views                 → Templates
build.sbt                → Application build script
conf                     → Configuration files and other non-compiled resources (on classpath)
 └ application.conf      → Main configuration file
 └ routes                → Routes definition
dist                     → Arbitrary files that should be included in your projects distribution
project                  → sbt configuration files
 └ build.properties      → Marker for sbt project
 └ plugins.sbt           → sbt plugins including the declaration for Play itself
public                   → Public assets
 └ stylesheets           → CSS files
 └ javascripts           → Javascript files
 └ images                → Image files
test                     → source folder for unit or functional tests
```
