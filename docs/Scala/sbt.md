---
title: SBT
category: Scala
tags: build tools
---

# SBT Links

[SBT Home Page](https://www.scala-sbt.org/)
[SBT Reference Manual](https://www.scala-sbt.org/1.x/docs/index.html)

## Create a New Project

```shell
$ sbt new scala/scala3.g8
$ cd hello-scala3
$ sbt
...
> run
> exit
```

## Modern build.sbt
```scala
val scala3Version = "3.3.0"

lazy val root = project
  .in(file("."))
  .settings(
    name := "scala3-simple",
    version := "0.1.0-SNAPSHOT",
    scalaVersion := scala3Version,
    libraryDependencies += "org.scalameta" %% "munit" % "0.7.29" % Test
  )
```
