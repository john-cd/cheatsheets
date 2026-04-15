---
title: Scala (Generalities)
category: Scala
tags: Scala
---

# Scala (Generalities)


## Main Features of Scala

- All types are objects
- Type inference
- Nested Functions
- Functions are objects
- Domain specific language (DSL) support
- Traits
- Closures
- Concurrency support inspired by Erlang

## Tools and Frameworks

REPL [https://ammonite.io/](https://ammonite.io/)

[https://scalafiddle.io/](https://scalafiddle.io/)

- [The Lift Framework](https://liftweb.net/)
- [The Play framework](https://www.playframework.com/)
- [The Bowler framework](https://github.com/bowler-framework/bowler-quickstart)
- [Akka](https://akka.io/)

[https://typelevel.org/](https://typelevel.org/)

## Install

- Need to have Java Software Development Kit (SDK) installed

```bash
java -version
```

```shell
export JAVA_HOME=/usr/local/java-current
export PATH=$PATH:$JAVA_HOME/bin/
```

[https://www.scala-lang.org/download/](https://www.scala-lang.org/download/)

### Compilation

```shell
scalac HelloWorld.scala  // produces HelloWorld.class
scala -classpath . HelloWorld
```

## Scala 3 Updates

- **Indentation-based syntax**: Similar to Python.
- **Enums**: First-class support for algebraic data types.
- **Extension Methods**: Easier way to add methods to existing types.
- **Given Instances and Using Clauses**: Replacement for `implicit`s.
