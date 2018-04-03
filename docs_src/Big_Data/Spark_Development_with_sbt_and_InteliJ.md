# Setup a Spark Development Environment with IntelliJ and sbt

## Useful Links

[ Hortonworks tutorial ]( https://hortonworks.com/tutorial/setting-up-a-spark-development-environment-with-scala/ )


## Packaging and Submission Steps using sbt 

Package a jar containing your application:

```shell
$ sbt package
...
[info] Packaging {..}/{..}/target/scala-2.11/simple-project_2.11-1.0.jar
```

Don't use ``sbt run`` 

Then use [spark submit] ( https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit )
 to run your application

```sh
YOUR_SPARK_HOME/bin/spark-submit \
  --class "SimpleApp" \
  --master local[4] \
  target/scala-2.11/simple-project_2.11-1.0.jar
```

Open the Spark UI to monitor: [ http://localhost:4040 ]( http://localhost:4040 )


## Plugins

### sbt-spark-package

The [ Sbt Plugin for Spark Packages ]( https://github.com/databricks/sbt-spark-package ) is a Sbt plugin that aims to simplify the use and development of Spark Packages.

[ Blog ]( https://medium.com/@mrpowers/creating-a-spark-project-with-sbt-intellij-sbt-spark-package-and-friends-cc9108751c28 )


### IntelliJ plugin for Spark 

Note: does not work with IntelliJ 2018.1

The [ IntelliJ plugin for Spark ]( https://plugins.jetbrains.com/plugin/10412-spark ) supports for deployment spark application and cluster monitoring. 

- To install, download the plugin
- File > Settings, Plugins tab, browse repos... point to the zip file

