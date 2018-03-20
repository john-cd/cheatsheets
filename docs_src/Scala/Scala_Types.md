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

// our refined instance (and type):
val refinedMockPersister = new Persister {  
  override def doPersist(e: Entity) = ()   
}
```

[Scala Types of Types](https://ktoso.github.io/scala-types-of-types/#refined-types-refinements)


## Generics

```scala
class Reference[T] {
    private var contents: T = _             // _ represents a default value. This default value is 0 for numeric types, false for the Boolean type, () for the Unit type and null for all object types.
    def set(value: T) { contents = value }
    def get: T = contents
}

trait Cache[K, V] {
      def get(key: K): V
      def put(key: K, value: V)
      def delete(key: K)
    }

def remove[K](key: K)  // function
```

## Type Variance

Covariance ``+A`` allow you to set the your container to a either a variable with the same type or parent type.

```scala
class MyContainer[+A](a: A)(implicit manifest: scala.reflect.Manifest[A]) {
      private[this] val item = a

      def get = item

      def contents = manifest.runtimeClass.getSimpleName
    }

    val fruitBasket: MyContainer[Fruit] = new MyContainer[Orange](new Orange())
    fruitBasket.contents
```

Contravariance ``-A`` is the opposite of covariance

Declaring neither -/+, indicates invariance variance.  You cannot use a superclass variable reference ("contravariant" position) or a subclass variable reference ("covariant" position) of that type.

## Upper and Lower Type Bounds

```scala
abstract class Pet extends Animal { def name: String }

class Cat extends Pet {
  override def name: String = "Cat"
}

class PetContainer[P <: Pet](p: P) {
  def pet: P = p   // The class PetContainer take a type parameter P which must be a subtype of Pet.
}
```

Lower type bounds declare a type to be a supertype of another type. The term ``B >: A`` expresses that the type parameter B or the abstract type B refer to a supertype of type A.


## Abstract Types

```scala
type R = Double // type alias
```

```scala
trait Container {
  type T
  val data: T

  def compare(other: T) = data.equals(other)
}

class StringContainer(val data: String) extends Container {
  override type T = String
}
```

### Generics vs Abstract Types

Generics:

- If you need just type instantiation. A good example is the standard collection classes.
- If you are creating a family of types.

Abstract types:

- If you want to allow people to mix in types using traits.
- If you need better readability in scenarios where both could be interchangeable.
- If you want to hide the type definition from the client code.

## Infix Type

We can make a type infix, meaning that a generic type with two type parameters can be displayed between two types.
The type specifier ``Pair[String,Int]`` can be written as ``String Pair Int``.

```scala
class Pair[A, B](a: A, b: B)

type ~[A,B] = Pair[A,B]
val pairlist: List[String ~ Int]   // operator-like usage

case class Item[T](i: T) {
	def ~(j: Item[T]) = new Pair(this, j)  // creating an infix operator method to use with our infix type
}

(Item("a") ~ Item("b")).isInstanceOf[String ~ String]
```

[ShapeLess](https://github.com/milessabin/shapeless)

## Structural Types

```scala
import scala.language.reflectiveCalls   // use reflection --> slow

def onlyThoseThatCanPerformQuacks(quacker: {def quack:String}): String = {
        "received message: %s".format(quacker.quack)
      }

type SpeakerAndMover = {def speak:String; def move(steps:Int, direction:String):String}  // with type aliasing
```

## Self-type

Self-types are a way to declare that a trait must be mixed into another trait, even though it doesn’t directly extend it. That makes the members of the dependency available without imports.

```scala
trait User {
  def username: String
}

trait Tweeter {
  this: User =>  // reassign this
  def tweet(tweetText: String) = println(s"$username: $tweetText")
}

class VerifiedTweeter(val username_ : String) extends Tweeter with User {  // We mixin User because Tweeter required it
  def username = s"real $username_"
}
```

### Difference between a self type and extending a trait

* If you say that B extends A, then B is an A. When you use self-types, B requires an A.

There are two specific requirements that are created with self-types:
1. If B is extended, then you're required to mix-in an A.
1. When a concrete class finally extends/mixes-in these traits, some class/trait must implement A.

```scala
trait Wrong extends Tweeter {
     def noCanDo = name        // does not compile
}
```

If Tweeter was a subclass of User, there would be no error. In the code above, we required a User whenever Tweeter is used, however a User wasn't provided to Wrong, so we got an error.

* Self types allow you to define cyclical dependencies. For example, you can achieve this:

```scala
trait A { self: B => }
trait B { self: A => }
```

Inheritance using extends does not allow that.

* Because self-types aren't part of the hierarchy of the required class they can be excluded from pattern matching, especially when you are exhaustively matching against a sealed hierarchy. This is convenient when you want to model orthogonal behaviors such as:

```scala
sealed trait Person
trait Student extends Person
trait Teacher extends Person
trait Adult { this : Person => } // orthogonal to its condition

val p : Person = new Student {}
p match {
  case s : Student => println("a student")
  case t : Teacher => println("a teacher")
} // that's it we're exhaustive
```

## Implicits

Implicits wrap around existing classes to provide extra functionality


```scala
object MyPredef {   // usually in a companion object

  class IntWrapper(val original: Int) {
	def isOdd = original % 2 != 0
	def isEven = !isOdd
  }

  implicit def thisMethodNameIsIrrelevant(value: Int) = new IntWrapper(value)
}

import MyPredef._
//imported implicits come into effect within this scope
19.isOdd

// Implicits can be used to automatically convert one type to another
import java.math.BigInteger
implicit def Int2BigIntegerConvert(value: Int): BigInteger = new BigInteger(value.toString)
def add(a: BigInteger, b: BigInteger) = a.add(b)
add(3, 6)  // 3 and 6 are Int

// Implicits function parameters
def howMuchCanIMake_?(hours: Int)(implicit amount: BigDecimal, currencyName: String) = (amount * hours).toString() + " " + currencyName
implicit var hourlyRate = BigDecimal(34.00)
implicit val currencyName = "Dollars"
howMuchCanIMake_?(30)
```

Default arguments though are preferred to Implicit Function Parameters.

## Context-bound Types

```scala
def inspect[T : TypeTag](l: List[T]) = typeOf[T].typeSymbol.name.decoded
val list = 1 :: 2 :: 3 :: 4 :: 5 :: Nil
inspect(list)
```

equivalent to

```scala
def inspect[T](l: List[T])(implicit tt: TypeTag[T]) = tt.tpe.typeSymbol.name.decoded
    val list = 1 :: 2 :: 3 :: 4 :: 5 :: Nil
    inspect(list)
```

TypeTags can be used to determine a type used before it erased by the VM by using an implicit TypeTag argument.


