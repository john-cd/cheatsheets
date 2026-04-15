---
title: Scala Database Access
category: Scala
tags: Scala, DB
---

# Scala Database Access


## Database Access / ORM Libraries

[Slick](https://slick.lightbend.com/)

* [Manual](https://slick.lightbend.com/doc/3.2.1/introduction.html)

[JOOQ](https://www.jooq.org/)

[Squeryl](https://squeryl.org/getting-started.html)

[SORM](https://sorm-framework.org/)

[Doobie](https://tpolecat.github.io/doobie/)

[ReactiveMongo](https://reactivemongo.org/)

[Comparison of multiple frameworks](
https://softwaremill.com/comparing-scala-relational-database-access-libraries/#summary)

## Database Initialization / Migration

[Flyway](https://flywaydb.org/)

## Modern Examples

### Slick

```scala
import slick.jdbc.H2Profile.api._
import scala.concurrent.ExecutionContext.Implicits.global

class Coffees(tag: Tag) extends Table[(String, Int, Double, Int, Int)](tag, "COFFEES") {
  def name = column[String]("COF_NAME", O.PrimaryKey)
  def supID = column[Int]("SUP_ID")
  def price = column[Double]("PRICE")
  def sales = column[Int]("SALES")
  def total = column[Int]("TOTAL")
  def * = (name, supID, price, sales, total)
}
val coffees = TableQuery[Coffees]
```

### Doobie
```scala
import doobie._
import doobie.implicits._

val program1 = sql"select 42".query[Int].unique
```

### Quill
```scala
import io.getquill._

lazy val ctx = new PostgresJdbcContext(SnakeCase, "ctx")
import ctx._

case class Person(id: Int, name: String, age: Int)

val q = quote {
  query[Person].filter(p => p.age > 18)
}
```
