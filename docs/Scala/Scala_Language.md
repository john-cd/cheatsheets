---
title: Scala Language
category: Scala
tags: Scala
---

## Links

- [Scala 3 Documentation](https://docs.scala-lang.org/scala3/book/introduction.html)
- [Scala Cheatsheet](https://docs.scala-lang.org/cheatsheets/)

## Scala 3 Features

### Enums
```scala
enum Color:
  case Red, Green, Blue
```

### Given Instances and Using Clauses
Replacing `implicits` for context parameters.
```scala
trait Ord[T]:
  def compare(x: T, y: T): Int

given intOrd: Ord[Int] with
  def compare(x: Int, y: Int) =
    if x < y then -1 else if x > y then 1 else 0

def max[T](x: T, y: T)(using ord: Ord[T]): T =
  if ord.compare(x, y) < 0 then y else x
```
