---
title: Akka / Pekko Cheatsheet
category: Scala
tags:
---

# Akka / Pekko

Apache Pekko is an open-source fork of Akka 2.6.x, created after Akka changed its license.

- [Pekko Documentation](https://pekko.apache.org/docs/pekko/current/)
- [Akka Documentation](https://doc.akka.io/docs/akka/current/)

Actors have:
- A mailbox (the queue where messages end up).
- A behavior (the state of the actor, internal variables etc.).
- Messages (pieces of data representing a signal, similar to method calls and their parameters).
- An execution environment (the machinery that takes actors that have messages to react to and invokes their message handling code).
- An address.

sbt dependencies (for Pekko):
```scala
libraryDependencies ++= Seq(
  "org.apache.pekko" %% "pekko-actor-typed" % "1.0.2",
  "org.apache.pekko" %% "pekko-stream" % "1.0.2"
)
```
