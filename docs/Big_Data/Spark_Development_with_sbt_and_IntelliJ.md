# Setup a Spark Development Environment with IntelliJ and sbt

## Project Setup

Create a new sbt project and add the Spark dependencies to your `build.sbt`:

```scala
scalaVersion := "2.12.18" // Or 2.13.x depending on your Spark version

val sparkVersion = "3.5.0"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion % "provided",
  "org.apache.spark" %% "spark-sql" % sparkVersion % "provided"
)
```

*Note:* Using `% "provided"` means you expect the Spark libraries to be present on the cluster where you submit the job, keeping your "fat jar" small. For local testing from within IntelliJ, you may need to temporarily remove `"provided"`.

## Packaging and Submission

Package a fat jar containing your application using the `sbt-assembly` plugin:

```shell
$ sbt assembly
...
[info] Packaging {..}/{..}/target/scala-2.12/simple-project-assembly-1.0.jar
```

*Note:* Do not use `sbt run` for Spark cluster applications.

Then use [spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit) to run your application:

```sh
YOUR_SPARK_HOME/bin/spark-submit \
  --class "SimpleApp" \
  --master local[4] \
  target/scala-2.12/simple-project-assembly-1.0.jar
```

Open the Spark UI to monitor: [https://localhost:4040](https://localhost:4040)

## IntelliJ Setup

Modern IntelliJ IDEA versions have built-in support for sbt and Scala.
1. Install the official Scala plugin.
2. Import the project by opening the `build.sbt` file.
3. Mark your `src/main/scala` folder as a Sources Root if it isn't automatically detected.

### Big Data Tools Plugin

The JetBrains [Big Data Tools plugin](https://plugins.jetbrains.com/plugin/12494-big-data-tools) provides integration for Spark, Hadoop, Zeppelin, and S3 right inside IntelliJ IDEA Ultimate.
