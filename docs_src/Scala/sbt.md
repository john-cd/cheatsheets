

# SBT

## Links

http://www.scala-sbt.org/

https://twitter.github.io/scala_school/sbt.html

https://github.com/shekhargulati/52-technologies-in-2016/blob/master/02-sbt/README.md

## Create a New Project

```shell
$ sbt new sbt/scala-seed.g8
$ cd hello
$ sbt
...
> run
> exit
```

## Layout

sbt uses the same directory structure as Maven for source files by default (all paths are relative to the base directory):

```
src/
  main/
    resources/
       <files to include in main jar here>
    scala/
       <main Scala sources>
    java/
       <main Java sources>
  test/
    resources
       <files to include in test jar here>
    scala/
       <test Scala sources>
    java/
       <test Java sources>
```

Other directories in ``src/`` will be ignored. Additionally, all hidden directories will be ignored.

Source code can be placed in the project’s base directory as ``hello/app.scala``, which may be for small projects, though for normal projects people tend to keep the projects in the src/main/ directory to keep things neat.


## Build Definition

The build definition goes in a file called ``build.sbt``, located in the project’s base directory. The “base directory” is the directory containing the project.
In addition to ``build.sbt``, the project directory can contain .scala files that defines helper objects and one-off plugins.

```
build.sbt
project/
  Dependencies.scala
```

``.gitignore`` (or equivalent for other version control systems) should contain:

```
target/
```

As part of your build definition, specify the version of ``sbt`` that your build uses. This allows people with different versions of the sbt launcher to build the same projects with consistent results. 
To do this, create a file named ``project/build.properties`` that specifies the sbt version as follows:

```
sbt.version=1.0.2
```

A build definition is defined in build.sbt, and it consists of a set of projects (of type Project). Because the term project can be ambiguous, we often call it a subproject.

```scala
lazy val root = (project in file("."))
  .settings(
    name := "Hello",
    scalaVersion := "2.12.3"
  )
```

Each subproject is configured by key-value pairs.

``build.sbt`` may also be interspersed with vals, lazy vals, and defs. Top-level objects and classes are not allowed in ``build.sbt``.
Those should go in the ``project/`` directory as Scala source files.

There are three flavors of key:

```
SettingKey[T]: a key for a value computed once (the value is computed when loading the subproject, and kept around).
TaskKey[T]: a key for a value, called a task, that has to be recomputed each time, potentially with side effects.
InputKey[T]: a key for a task that has command line arguments as input. Check out Input Tasks for more details.
```

### Built-in Keys 

The built-in keys are just fields in an object called Keys. A ``build.sbt`` implicitly has an ``import sbt.Keys._``, so sbt.Keys.name can be referred to as name.


### Adding Library Dependencies 

To depend on third-party libraries, there are two options. The first is to drop jars in ``lib/`` (unmanaged dependencies) and the other is to add managed dependencies, which will look like this in ``build.sbt``:

```scala
val derby = "org.apache.derby" % "derby" % "10.4.1.3"

lazy val commonSettings = Seq(
  organization := "com.example",
  version := "0.1.0-SNAPSHOT",
  scalaVersion := "2.12.3"
)

lazy val root = (project in file("."))
  .settings(
    commonSettings,
    name := "Hello",
    libraryDependencies += derby
  )
```

The libraryDependencies key involves two complexities: ``+=`` rather than ``:=``, and the ``%`` method. ``+=`` appends to the key’s old value rather than replacing it. 
The ``%`` method is used to construct an Ivy module ID from strings.
