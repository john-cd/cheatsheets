---
title: Scala Testing
category: Scala
tags: Scala, Tests
---

## Links

- [ScalaTest](https://www.scalatest.org/)
- [MUnit](https://scalameta.org/munit/)

## ScalaTest Example (Scala 3)

```scala
import org.scalatest.funsuite.AnyFunSuite

class SetSuite extends AnyFunSuite:
  test("An empty Set should have size 0") {
    assert(Set.empty.size == 0)
  }

  test("Invoking head on an empty Set should produce NoSuchElementException") {
    assertThrows[NoSuchElementException] {
      Set.empty.head
    }
  }
```

## MUnit Example
MUnit is a popular testing library for Scala 3.
```scala
class MySuite extends munit.FunSuite {
  test("hello") {
    val obtained = 42
    val expected = 43
    assertEquals(obtained, expected)
  }
}
```
