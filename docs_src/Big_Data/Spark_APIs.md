

## DataFrames APIs

DataFrame operations: 

- printSchema()
- select()
- show()
- count()
- groupBy()
- sum()
- limit()
- orderBy()
- filter()
- withColumnRenamed()
- join()
- withColumn()

Example:

```scala
// In the Regular Expression below:
// ^  - Matches beginning of line
// .* - Matches any characters, except newline

df
 .filter($"article".rlike("""^Apache_.*"""))
 .orderBy($"requests".desc)
 .show() // By default, show will return 20 rows

// Import the sql functions package, which includes statistical functions like sum, max, min, avg, etc.
import org.apache.spark.sql.functions._

df.groupBy("project").sum().show()
```

### Columns

A new column is constructed based on the input columns present in a dataframe:

```scala
df("columnName") 			// On a specific DataFrame.
col("columnName") 			// A generic column no yet associated with a DataFrame.
col("columnName.field") 	// Extracting a struct field
col("`a.column.with.dots`") // Escape `.` in column names.
$"columnName" 				// Scala short hand for a named column.
expr("a + 1") 				// A column that is constructed from a parsed SQL Expression.
lit("abc") 					// A column that produces a literal (constant) value.
```

Column objects can be composed to form complex expressions:

```scala
$"a" + 1
$"a" === $"b"
```

### File Read

CSV - Create a DataFrame with the anticipated structure

```scala
val clickstreamDF = sqlContext.read.format("com.databricks.spark.csv")
  .option("header", "true")
  .option("delimiter", "\\t")
  .option("mode", "PERMISSIVE")
  .option("inferSchema", "true")
  .load("dbfs:///databricks-datasets/wikipedia-datasets/data-001/clickstream/raw-uncompressed")
```
  
PARQUET - To create Dataset[Row] using SparkSession

```scala
val people = spark.read.parquet("...")
val department = spark.read.parquet("...")

people.filter("age > 30")
  .join(department, people("deptId") === department("id"))
  .groupBy(department("name"), "gender")
  .agg(avg(people("salary")), max(people("age")))
```

### Repartitioning / Caching

```scala
val clickstreamNoIDs8partDF = clickstreamNoIDsDF.repartition(8)
clickstreamNoIDs8partDF.registerTempTable("Clickstream")
sqlContext.cacheTable("Clickstream")
```

An ideal partition size in Spark is about 50 MB - 200 MB.
The cache gets stored in Project Tungsten binary compressed columnar format.
