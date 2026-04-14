---
title: Play Framework
category: Scala
tag: Scala Akka Play Web REST
---

## Links

[Play Framework](https://playframework.com/documentation/)

## The Play application layout

The layout of a Play application is standardized to keep things as simple as possible. After a first successful compile, a Play application looks like this:

```txt
app                      → Application sources
 └ assets                → Compiled asset sources
    └ stylesheets        → Typically LESS CSS sources
    └ javascripts        → Typically CoffeeScript sources
 └ controllers           → Application controllers
 └ models                → Application business layer
 └ views                 → Templates
build.sbt                → Application build script
conf                     → Configurations files and other non-compiled resources (on classpath)
 └ application.conf      → Main configuration file
 └ routes                → Routes definition
dist                     → Arbitrary files to be included in your projects distribution
public                   → Public assets
 └ stylesheets           → CSS files
 └ javascripts           → Javascript files
 └ images                → Image files
project                  → sbt configuration files
 └ build.properties      → Marker for sbt project
 └ plugins.sbt           → sbt plugins including the declaration for Play itself
lib                      → Unmanaged libraries dependencies
logs                     → Logs folder
 └ application.log       → Default log file
target                   → Generated stuff
 └ resolution-cache      → Info about dependencies
 └ scala-2.11
    └ api                → Generated API docs
    └ classes            → Compiled class files
    └ routes             → Sources generated from routes
    └ twirl              → Sources generated from templates
 └ universal             → Application packaging
 └ web                   → Compiled web assets
test                     → source folder for unit or functional tests
```

## Play 3.x
Play 3.0 uses Apache Pekko instead of Akka.

[Play Framework Documentation](https://www.playframework.com/documentation/3.0.x/Home)

## Play

[Angular 2+ with Play Framework 2.6.x – Yohan Gomez – Medium](https://medium.com/@yohan.gz/https-medium-com-yohan-gz-angular-with-play-framework-a6c3f8b339f3)

[yohangz-scala-play-angular-seed- Scala Play 2.6.x + Angular 5 with Angular CLI seed project with full-fledged build process](https://github.com/yohangz/scala-play-angular-seed)

[Getting Started With Play Framework - DZone - Refcardz](https://dzone.com/refcardz/getting-started-play-framework?chapter=10)

[How Visier Accelerates Developer Productivity with Play Framework, Typescript and Angular 2 - @lightbend](https://www.lightbend.com/blog/getting-started-with-angular-2)

[jamesward-play-rest-security](https://github.com/jamesward/play-rest-security)

[joost-de-vries-play-angular-typescript.g8- A giter8 template for a Play Angular 4 Typescript application](https://github.com/joost-de-vries/play-angular-typescript.g8)

[play-angular-typescript.g8-app.module.ts at master · joost-de-vries-play-angular-typescript.g8](https://github.com/joost-de-vries/play-angular-typescript.g8/blob/master/src/main/g8/app/assets/app/app.module.ts)

[playframework-play-scala-secure-session-example- An example Play application showing encrypted session management](https://github.com/playframework/play-scala-secure-session-example)
