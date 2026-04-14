---
title: Scala Types
category: Scala
tags: Scala
---

## Type Refinement

Type Refinement = "subclassing without naming the subclass".

```scala
class Entity

trait Persister {
  def doPersist(e: Entity) = {
    e.persistForReal()
  }
}
```

## Scala 3 Types

### Union Types
Union types allow a value to be one of multiple types.
```scala
def help(id: UserName | Password) =
  val user = id match
    case UserName(name) => lookupName(name)
    case Password(hash) => lookupPassword(hash)
```

### Intersection Types
Intersection types replace compound types (`A with B`).
```scala
trait Resettable:
  def reset(): Unit

trait Growable[T]:
  def add(x: T): Unit

def f(x: Resettable & Growable[String]) =
  x.reset()
  x.add("first")
```
