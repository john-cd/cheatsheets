---
title: Scala Collections
category: scala
tags:
---

Examples from [Scala Koans](htpp://scalakoans.org).

## Core Packages

The scala package contains core types like Int, Float, Array or Option which are accessible in all Scala compilation units without explicit qualification or imports.

Notable packages include:

	scala.collection and its sub-packages contain Scala's collections framework
	scala.collection.immutable - Immutable, sequential data-structures such as Vector, List, Range, HashMap or HashSet
	scala.collection.mutable - Mutable, sequential data-structures such as ArrayBuffer, StringBuilder, HashMap or HashSet
	scala.collection.concurrent - Mutable, concurrent data-structures such as TrieMap
	scala.collection.parallel.immutable - Immutable, parallel data-structures such as ParVector, ParRange, ParHashMap or ParHashSet
	scala.collection.parallel.mutable - Mutable, parallel data-structures such as ParArray, ParHashMap, ParTrieMap or ParHashSet
	
	scala.concurrent - Primitives for concurrent programming such as Futures and Promises
	scala.io - Input and output operations
	scala.math - Basic math functions and additional numeric types like BigInt and BigDecimal
	scala.sys - Interaction with other processes and the operating system
	scala.util.matching - Regular expressions


Additional parts of the standard library are shipped as separate libraries. These include:

	scala.reflect - Scala's reflection API (scala-reflect.jar)
	scala.xml - XML parsing, manipulation, and serialization (scala-xml.jar)
	scala.swing - A convenient wrapper around Java's GUI framework called Swing (scala-swing.jar)
	scala.util.parsing - Parser combinators (scala-parser-combinators.jar)
	Automatic imports

Identifiers in the scala package and the scala.Predef object are always in scope by default.

Some of these identifiers are type aliases provided as shortcuts to commonly used classes. For example, List is an alias for scala.collection.immutable.List.

Other aliases refer to classes provided by the underlying platform. For example, on the JVM, String is an alias for java.lang.String.


## Traversables

Traversables are the superclass of Lists, Arrays, Maps, Sets, Streams, and more.
The methods involved can be applied to each other in a different type.  

```scala
val set = Set(1, 9, 10, 22)
val list = List(3, 4, 5, 10)
val result = set ++ list  		// ++ appends two Traversables together.
result.size
result.isEmpty
result.hasDefiniteSize  		// false if a Stream
```

- Take some

```scala
list.head
list.headOption
list.tail
list.lastOption
result.last
list.init						// collection without the last element
list.slice(1, 3)
list.take(3)
list drop 6 take 3
list.takeWhile(_ < 100)
list.dropWhile(_ < 100)
```

- Filter, Map, Flatten

```scala
list.filter(_ < 100)
list.filterNot(_ < 100)
list.find(_ % 2 != 0) 						// get first element that matches

list.foreach(num => println(num * 4))		// side effect

list.map(_ * 4)								// map

val list = List(List(1), List(2, 3, 4), List(5, 6, 7), List(8, 9, 10))
list.flatten
list.flatMap(_.map(_ * 4))  				// map then flatten

val result = list.collect {					// apply a partial function to all elements of a Traversable and will return a different collection.
      case x: Int if (x % 2 == 0) => x * 3
    }
// can use  orElse  or andThen
```

- Split

```scala
val array = Array(87, 44, 5, 4, 200, 10, 39, 100)  // splitAt - will split a Traversable at a position, returning a tuple.
val result = array splitAt 3
result._1
result._2

val result = array partition (_ < 100) 				// partition will split a Traversable according to predicate, return a 2 product Tuple. The left side are the elements satisfied by the predicate, the right side is not.  

// groupBy returns a map e.g. Map( "Odd" -> ... , "Even" -> ...)
val result = array groupBy { case x: Int if x % 2 == 0 => "Even"; case x: Int if x % 2 != 0 => "Odd" } 
```

- Analyze

```scala
list forall (_ < 100) 						// true if predicate true for all elements
list exists (_ < 100) 						// true if predicate true for any element
list count (_ < 100)
```

- Reduce and Fold

```scala
list.foldLeft(0)(_ - _)
(0 /: list)(_ - _) 							// Short hand

list.foldRight(0)(_ - _)				
(list :\ 0)(_ - _) 							// Short hand

list.reduceLeft { _ + _ } 
list.reduceRight { _ + _ }

list.sum 
list.product
list.max
list.min

val list = List(List(1, 2, 3), List(4, 5, 6), List(7, 8, 9))
list.transpose
```

- Conversions; toList, as well as other conversion methods like toSet, toArray will not convert if the collection type is the same.

```scala
list.toArray
list.toSet
set.toList
set.toIterable
set.toSeq
set.toIndexedSeq
list.toStream

val list = List("Phoenix" -> "Arizona", "Austin" -> "Texas")  // elements should be tuples
val result = list.toMap
```

- Print

```scala
result.mkString(",")
list.mkString(">", ",", "<")
val list = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
stringBuilder.append("I want all numbers 6-12: ")
list.filter(it => it > 5 && it < 13).addString(stringBuilder, ",")
stringBuilder.mkString 
```

## Lists

```scala
val a = List(1, 2, 3)  		// immutable
val b = 1 :: 2 :: 3 :: Nil  // cons notation 
(a == b) 	// true
a eq b   	// false
a.length
a.head
a.tail
a.reverse					// reverse the list
a.map {v => v * 2}   		// or a.map {_ * 2} or a.map(_ * 2)
a.filter {v => v % 3 == 0}
a.filterNot(v => v == 5) 	// remove where value is 5
a.reduceLeft(_ + _)			// note the two _s below indicate the first and second args respectively
a.foldLeft(10)(_ + _)		// foldlLeft is like reduce, but with an explicit starting value
(1 to 5).toList				// from range
val a = a.toArray
```

Nil lists are identical, even of different types

## Iterators

```scala
val list = List(3, 5, 9, 11, 15, 19, 21)
val it = list.iterator
if (it.hasNext) {
  it.next should be(__)
}

val it = list grouped 3 		// `grouped` will return an fixed sized Iterable chucks of an Iterable
val it = list sliding 3			// `sliding` will return an Iterable that shows a sliding window of an Iterable.	
val it = list sliding(3, 3) 	// `sliding` can take the size of the window as well the size of the step during each iteration
list takeRight 3
list dropRight 3

val xs = List(3, 5, 9)			// `zip` will stitch two iterables into an iterable of pairs (tuples) of corresponding elements from both iterables.
val ys = List("Bob", "Ann", "Stella")
xs zip ys

// If two Iterables aren't the same size, then `zip` will only zip what can only be paired.
xs zipAll(ys, -1, "?")  // if two Iterables aren't the same size, then `zipAll` can provide fillers

xs.zipWithIndex
```

## Arrays, Sequences

```scala
val a = Array(1, 2, 3)
val s = a.toSeq
val l = s.toList
```

```scala
val s = Seq("hello", "to", "you")
val filtered = s.filter(_.length > 2)
val r = s map {
      _.reverse
    }
val s = for (v <- 1 to 10 if v % 3 == 0) yield v  // create a sequence from a for comprehension with an optional condition
s.toList
```

## Lazy Collections and Streams

```scala
val strictList = List(10, 20, 30)
val lazyList = strictList.view		// Strict collection always processes its elements but lazy collection does it on demand

val infinite = Stream.from(1)
infinite.take(4).sum
Stream.continually(1).take(4).sum

// Always remember tail of a lazy collection is never computed unless required

def makeLazy(value: Int): Stream[Int] = {
  Stream.cons(value, makeLazy(value + 1))
}
val stream = makeLazy(1)
stream.head
```

## Maps

```scala
val myMap = Map("MI" -> "Michigan", "OH" -> "Ohio", "WI" -> "Wisconsin", "MI" -> "Michigan")

// access by key - Accessing a map by key results in an exception if key is not found
myMap("MI")									
myMap.contains("IL") 

val aNewMap = myMap + ("IL" -> "Illinois")  // add - creates a new collection if immutable
val aNewMap = myMap - "MI"  				// remove - Attempted removal of nonexistent elements from a map is handled gracefully
val aNewMap = myMap -- List("MI", "OH")     // remove multiples
val aNewMap = myMap - ("MI", "WI") // Notice: single '-' operator for tuples

var anotherMap += ("IL" -> "Illinois") 		// compiler trick - creates a new collection and reassigns; note the 'var' 

// Map values can be iterated
val mapValues = myMap.values
mapValues.size
mapValues.head
mapValues.last

for (mval <- mapValues) println(mval)
// NOTE that the following will not compile, as iterators do not implement "contains"
//mapValues.contains("Illinois")

// Map keys may be of mixed type
val myMap = Map("Ann Arbor" -> "MI", 49931 -> "MI")

// Mixed type values can be added to a map
val myMap = scala.collection.mutable.Map.empty[String, Any]
myMap("Ann Arbor") = (48103, 48104, 48108)
myMap("Houghton") = 49931

// Map equivalency is independent of order
val myMap1 = Map("MI" -> "Michigan", "OH" -> "Ohio", "WI" -> "Wisconsin", "IA" -> "Iowa")
val myMap2 = Map("WI" -> "Wisconsin", "MI" -> "Michigan", "IA" -> "Iowa", "OH" -> "Ohio")
myMap1.equals(myMap2)
```

Maps insertion with duplicate key updates previous entry with subsequent value

- Mutable Maps

```scala
val myMap = mutable.Map("MI" -> "Michigan", "OH" -> "Ohio", "WI" -> "Wisconsin", "IA" -> "Iowa")
// same methods than immutable maps work
val myMap += ("IL" -> "Illinois")		// this is a method; note the difference from immutable += 
myMap.clear() 							// Convention is to use parens if possible when method called changes state
```

## Sets

```scala
val mySet = Set(1, 3, 4, 9)  // immutable
val mySet = mutable.Set("Michigan", "Ohio", "Wisconsin", "Iowa")
mySet.size
mySet contains "Ohio"
mySet += "Oregon"
mySet += ("Iowa", "Ohio")
mySet ++= List("Iowa", "Ohio")
mySet -= "Ohio"
mySet --= List("Iowa", "Ohio")
mySet.clear()  // mutable only

var sum = 0
for (i <- mySet)	// for comprehension
  sum = sum + i  	// of course this is the same thing as mySet.reduce(_ + _)
  
val mySet2 = Set("Wisconsin", "Michigan", "Minnesota")
mySet intersect mySet2  // or & operator
mySet1 union mySet2    // or | operator
mySet2 subsetOf mySet1
mySet1 diff mySet2
mySet1.equals(mySet2)  // independent of order
```

## Option[T]

```scala
val someValue: Option[String] = Some("I am wrapped in something")
val nullValue: Option[String] = None
someValue.get  						// java.util.NoSuchElementException if None
nullValue getOrElse "No value" 
nullValue.isEmpty

val value = someValue match { 		// pattern matching
      case Some(v) => v
      case None => 0.0
    }
```

- Option is more than just a replacement of null, its also a collection.

```scala
    Some(10) filter { _ == 10}
    Some(Some(10)) flatMap { _ map { _ + 10}}
	var newValue1 = 0
    Some(20) foreach { newValue1 = _}
```

- flatMap of Options will filter out all Nones and keep the Somes

```scala
val list = List(1, 2, 3, 4, 5)
val result = list.flatMap(it => if (it % 2 == 0) Some(it) else None)
```

- Using "for comprehension"

```scala
    val values = List(Some(10), Some(20), None, Some(15))
    val newValues = for {
      someValue <- values
      value <- someValue
    } yield value
```

## Java Interop

Scala can implicitly convert from a Scala collection type into a Java collection type. 

```scala
import scala.collection.JavaConversions._
```
