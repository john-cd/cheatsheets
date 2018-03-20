---
title: Scala (Generalities)
category: Scala
tags: Scala
---

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

REPL [http://ammonite.io/](http://ammonite.io/)

[https://scalafiddle.io/](https://scalafiddle.io/)

- [The Lift Framework]( https://liftweb.net/ )
- [The Play framework]( https://www.playframework.com/ )
- [The Bowler framework]( https://github.com/bowler-framework/bowler-quickstart )
- [Akka]( http://akka.io/ )

[https://typelevel.org/](https://typelevel.org/)

  
## Install

* Need to have Java Software Development Kit (SDK) installed 

```
java -version
```

```shell
export JAVA_HOME=/usr/local/java-current
export PATH=$PATH:$JAVA_HOME/bin/
```

[http://www.scala-lang.org/download/](http://www.scala-lang.org/download/)

### Compilation

```shell
scalac HelloWorld.scala  // produces HelloWorld.class
scala -classpath . HelloWorld
```
