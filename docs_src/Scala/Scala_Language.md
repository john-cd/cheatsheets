---
title: Scala Language
category: Scala
tags: Scala
---


## Links

- [Scala Cheatsheet]( http://docs.scala-lang.org/cheatsheets/ )
- [Scala @ TutorialPoint]( https://www.tutorialspoint.com/scala/index.htm )
- [Scala Tutorial (PDF)]( http://www.scala-lang.org/docu/files/ScalaTutorial.pdf )

Some examples are derived from [Scala Koans](http://www.scalakoans.org/).

## Basics

### Style

Class Names - For all class names, the first letter should be in Upper Case. If several words are used to form a name of the class, each inner word's first letter should be in Upper Case.

``class MyFirstScalaClass``

Method Names - All method names should start with a Lower Case letter. If multiple words are used to form the name of the method, then each inner word's first letter should be in Upper Case.

``def myMethodName()``

Program File Name - Name of the program file should exactly match the object name. When saving the file you should save it using the object name (Remember Scala is case-sensitive) and append ".scala" to the end of the name. If the file name and the object name do not match your program will not compile.

Assume 'HelloWorld' is the object name: the file should be saved as 'HelloWorld.scala'.


### Packages

```scala
package pkg 		// at start of file
package pkg { ... }	// bracket style
```

### Imports

```scala
import scala.collection._	                // wildcard import. When importing all the names of a package or class, one uses the underscore character (_) instead of the asterisk (*).
import scala.collection.Vector              // one class import
import scala.collection.{Vector, Sequence}	// selective import. Multiple classes can be imported from the same package by enclosing them in curly braces
import scala.collection.{Vector => Vec28}	// renaming import.
import java.util.{Date => _, _}	            // import all from java.util except Date.
```

All classes from the java.lang package are imported by default. The Predef object provides definitions that are accessible in all Scala compilation units without explicit qualification:
- immutable Map, Set, List, ::, Nil, print, println, assert, assume, require, ensuring

```scala
import scala.collection.mutable.HashMap               // Mutable collections must be imported.
import scala.collection.immutable.{TreeMap, TreeSet}  // So are specialized collections.
```

### Application Entry Point

```scala
object HelloWorld {
    def main(args: Array[String]) {
        println("Hello, world!")
    }
}
```

### Blocks

You can combine expressions by surrounding them with {}. We call this a block.
The result of the last expression in the block is the result of the overall block, too.

```scala
println({
  val x = 1 + 1
  x + 1
}) // 3
```

### Variables and Values

```scala
var x = 5 // variable
val x = 5 // immutable value / "const"
var x: Double = 5 // explicit type
println(x)
```

A lazy val is assignment that will not evaluated until it is called. Note there is no lazy var

```scala
lazy val a = {heavymath(); 19}
```

### Literals

```scala
val a = 2		// int
val b = 31L     // long
val c = 0x30B   // hexadecimal
val d = 3f		// float
val e = 3.22d	// double
val f = 93e-9
val g = 'a'			// character
val h = '\u0061' 	// unicode for a
val i = '\141' 		// octal for a
val j = '\"'		// escape sequences
val k = '\\'
val s = "To be or not to be"  	// string
s.charAt(0)
val s2 = """An apple a day
keeps the doctor away"""		// multi-lines string
s2.split('\n')
val s3 = """An apple a day
           |keeps the doctor away"""  // Multiline String literals can use | to specify the starting position of subsequent lines, then use stripMargin to remove the surplus indentation.
s3.stripMargin
```

### Enumerations

```scala
object Planets extends Enumeration {
  val Mercury = Value
  val Venus = Value
  val Earth = Value
  val Mars = Value
  val Jupiter = Value
  val Saturn = Value
  val Uranus = Value
  val Neptune = Value
  val Pluto = Value
}

Planets.Mercury.id
Planets.Mercury.toString //How does it get the name? by Reflection.

object GreekPlanets extends Enumeration {
  val Mercury = Value(1, "Hermes")   // enumeration with your own index and/or your own Strings
  val Venus = Value(2, "Aphrodite")
  //Fun Fact: Tellus is Roman for (Mother) Earth
  val Earth = Value(3, "Gaia")
  val Mars = Value(4, "Ares")
  val Jupiter = Value(5, "Zeus")
  val Saturn = Value(6, "Cronus")
  val Uranus = Value(7, "Ouranus")
  val Neptune = Value(8, "Poseidon")
  val Pluto = Value(9, "Hades")
}
```

### Common Data Structures

```scala
(1,2,3)	                	// tuple literal. (Tuple3)
var (x,y,z) = (1,2,3)		// destructuring bind: tuple unpacking via pattern matching.
// BAD var x,y,z = (1,2,3)	// hidden error: each assigned to the entire tuple.

val tuple = ("apple", 3)	// mixed type tuple
tuple._1
tuple._2
tuple.swap
```

```scala
var xs = List(1,2,3)		// list (immutable).
xs(2)	                	// paren indexing
1 :: List(2,3)				// cons (create a new list by prepending the element).

1 to 5                  	// Range sugar. Same as `1 until 6`
1 to 10 by 2
Range(1, 10, 2) 			// Range does not include the last item, even in a step increment
Range(1, 9, 2).inclusive
```

```scala
() 							// (empty parens)	sole member of the Unit type (like C/Java void).
```

### Control Constructs

```scala
if (check) happy else sad	// conditional.
if (check) happy            //
if (check) happy else ()	// same as above
while (x < 5) { println(x); x += 1}	// while loop.
do { println(x); x += 1} while (x < 5)	// do while loop.

for (x <- xs if x%2 == 0) yield x*10 	// for comprehension with guard
xs.filter(_%2 == 0).map(_*10)	     	// same as filter/map
for ((x,y) <- xs zip ys) yield x*y   	// for comprehension: destructuring bind
(xs zip ys) map { case (x,y) => x*y }	// same as
for (x <- xs; y <- ys) yield x*y     	// for comprehension: cross product. Later generators varying more rapidly than earlier ones
xs flatMap {x => ys map {y => x*y}}  	// same as
for (x <- xs; y <- ys) {
  println("%d/%d = %.1f".format(x, y, x/y.toFloat))		// for comprehension: imperative-ish
}
for (i <- 1 to 5) {						// for comprehension: iterate including the upper bound
  println(i)
}
for (i <- 1 until 5) {					// for comprehension: iterate omitting the upper bound
  println(i)
}

import scala.util.control.Breaks._		// break
breakable {
  for (x <- xs) {
    if (Math.random < 0.1) break
  }
}
```

### Formatting and Interpolation

```scala
val helloMessage = "Hello World"
s"Application $helloMessage"  // string interpolation; can include expressions which can include numbers and strings
// use `f` prefix before the string instead of an `s` for sprintf formatting
```

## Functions

Scala is a functional language in the sense that every function is a value and every value is an object so ultimately every function is an object.
Scala provides a lightweight syntax for defining anonymous functions, it supports higher-order functions, it allows functions to be nested, and supports currying.

```scala
def add(x: Int, y: Int): Int = x + y  	// the return type is declared after the parameter list and a colon

// GOOD def f(x: Any) = println(x)
// BAD  def f(x) = println(x)			// syntax error: need types for every arg.

def f(x: Int) = { 						// inferred return type
  val square = x*x
  square.toString
  } // The last expression in the body is the method’s return value. (Scala does have a return keyword, but it’s rarely used.)

// BAD def f(x: Int) { x*x }  hidden error: without = it’s a Unit-returning procedure; causes havoc

// When performing recursion, the return type on the method is mandatory!
```

- Backticks for reserved keywords and identifiers with a space (rare)

```scala
def `put employee on probation`(employee: Employee) = {
       new Employee(employee.`first name`, employee.`last name`, "Probation")
    }
```

### Multiple parameter lists or none at all

```scala
def addThenMultiply(x: Int, y: Int)(multiplier: Int): Int = (x + y) * multiplier
def name: String = System.getProperty("name")
```

### Procedures

```scala
def foo(x: Int) { //Note: No `=`; returns Unit
      print(x.toString)
    }
def foo(x: Int): Unit =  print(x.toString)  // or
```

Convention (not required for the compiler) states that if you a call a method that returns a Unit / has a side effect, invoke that method with empty parenthesis, other leave the parenthesis out

```scala
def performSideEffect():Unit = System.currentTimeMillis
performSideEffect()
```

### Default and named parameters

```scala
def addColorsWithDefaults(red: Int = 0, green: Int = 0, blue: Int = 0) = {
  (red, green, blue)
}

me.addColors(blue = 40)
```

###  Variable Length Arguments

```scala
def sum(args: Int*) = args.reduceLeft(_+_)				// varargs. must be last arg

def capitalizeAll(args: String*) = {
      args.map { arg =>
        arg.capitalize
      }
    }

capitalizeAll("rarity", "applejack")
```

If you want a collection expanded into a vararg, add ``:_*``

```scala
def repeatedParameterMethod(x: Int, y: String, z: Any*) = {
    "%d %ss can give you %s".format(x, y, z.mkString(", "))
  }

repeatedParameterMethod(3, "egg", List("a delicious sandwich", "protein", "high cholesterol"):_*) should be(__)
```

### Tail recursion

As a precaution, the helpful @tailrec annotation will throw a compile time if a method is not tail recursive,
meaning that the last call and only call of the method is the recursive method. Scala optimizes recursive calls
to a loop from a stack

```scala
import scala.annotation.tailrec //	importing annotation!
@tailrec						//  compiler will check that the function is tail recursive
def factorial(i: BigInt): BigInt = {
      @tailrec
      def fact(i: BigInt, accumulator: BigInt): BigInt = { 	// methods can be placed inside in methods; return type is obligatory
        if (i <= 1)
          accumulator
        else
          fact(i - 1, i * accumulator)
      }
      fact(i, 1)
    }

factorial(3)
```

### Infix, Postfix and Prefix Notations; Operators

```scala
object FrenchDate {
    def main(args: Array[String]) {
        val now = new Date
        val df = getDateInstance(LONG, Locale.FRANCE)
    println(df format now)       // Methods taking one argument can be used with an infix syntax. Equivalent to df.format(now)
    }
}
```

``1 + 2 * 3 / x`` consists exclusively of method calls, because it is equivalent to the following expression: ``(1).+(((2).*(3))./(x))``
This also means that +, *, etc. are valid identifiers in Scala.

Infix Operators do NOT work if an object has a method that takes two parameters.

```scala
 val g: Int = 31
 val s: String = g toHexString  // Postfix operators work if an object has a method that takes no parameters
```

Prefix operators work if an object has a method name that starts with unary_
```scala
class Stereo {
      def unary_+ = "on"
      def unary_- = "off"
    }

val stereo = new Stereo
+stereo   // it is on
```

Methods with colons are right-associative, that means the object that a method is on will be on the _right_ and the method parameter will be on the _left_

```scala
class Foo (y:Int) {
      def ~:(n:Int) = n + y + 3
    }

val foo = new Foo(9)
10 ~: foo
foo.~:(10)  // same as
```

### Anonymous Functions

```scala
def lambda = (x: Int) => x + 1

// other variants
def lambda2 = { x: Int => x + 1 }
val lambda3 = new Function1[Int, Int] {
      def apply(v1: Int): Int = v1 + 1
    }

val everything = () => 42   					// without parameter
val add = (x: Int, y: Int) => x + y				// multiple parameters

(1 to 5).map(_*2)          						// underscore notation.
(1 to 5) map (_*2)								// same with infix sugar.
(1 to 5).reduceLeft( _+_ )						// underscores are positionally matched 1st and 2nd args.
(1 to 5).map( x => x*x )						// to use an arg twice, have to name it.
(1 to 5).map { x => val y = x*2; println(y); y }	// block style returns last expression.
(1 to 5) filter {_%2 == 0} map {_*2}            // pipeline style (works with parens too).

// GOOD (1 to 5).map(2*)
// BAD (1 to 5).map(*2)	                        // anonymous function: bound infix method. Use 2*_ for sanity’s sake instead.

def compose(g: R => R, h: R => R) = (x:R) => g(h(x))
val f = compose({_*2}, {_-1})					// anonymous functions: to pass in multiple blocks, need outer parens.
```

Passing anonymous functions as parameter:

```scala
def makeWhatEverYouLike(xs: List[String], func: String => String) = {
      xs map func
    }
```

Function returning another function using an anonymous function:

```scala
def add(x: Int) = (y:Int) => x + y
```

Function Values:

```scala
object Timer {
    def oncePerSecond(callback: () => Unit) {        // () => T is a Function type that takes a Unit type. Unit is known as 'void' to a Java programmer.
        while (true) { callback(); Thread sleep 1000 }
    }

    def timeFlies() {
        println("time flies like an arrow...")
    }

    def main(args: Array[String]) {
        oncePerSecond(timeFlies)       // function value; could also be () => timeFlies()
    }
}
```

### By-name parameter

This is used extensively in scala to create blocks.

```scala
    def calc(x: => Int): Either[Throwable, Int] = {   //x is a call by name parameter; delayed execution of x
      try {
        Right(x)
      } catch {
        case b: Throwable => Left(b)
      }
    }

    val y = calc {                                    //This looks like a natural block
      println("Here we go!")                          //Some superfluous call
      49 + 20
    }
```

By name parameters can also be used with an Object and apply to make interesting block-like calls

```scala
object PigLatinizer {
      def apply(x: => String) = x.tail + x.head + "ay"
    }

val result = PigLatinizer {
      val x = "pret"
      val z = "zel"
      x ++ z //concatenate the strings
    }
```

### Closures

```scala
var incrementer = 1

def closure = {
  x: Int => x + incrementer
}
```

### Currying

```scala
val zscore = (mean: R, sd: R) => (x:R) => (x-mean)/sd		// currying, obvious syntax.
def zscore(mean: R, sd: R) = (x: R) => (x-mean)/sd	        // currying, obvious syntax
def zscore(mean: R, sd: R)(x: R) = (x-mean)/sd	        	// currying, sugar syntax. but then:
val normer = zscore(7, 0.4) _	                        	// need trailing underscore to get the partial, only for the sugar version.
def mapmake[T](g: T => T)(seq: List[T]) = seq.map(g)		// generic type.

def multiply(x: Int, y: Int) = x * y
val multiplyCurried = (multiply _).curried					
multiply(4, 5)
multiplyCurried(3)(2)
```

### Partial Applications

```scala
def adder(m: Int, n: Int) = m + n
val add2 = adder(2, _:Int)  // You can partially apply any argument in the argument list, not just the last one.
add2(3)    // which is 5

val add3 = adder _				// underscore to convert from a function to a lambda
adder(1, 9)
add3(1, 9)
```

### Partial Functions

```scala
val doubleEvens: PartialFunction[Int, Int] = new PartialFunction[Int, Int] {   // full declaration
      //States that this partial function will take on the task
      def isDefinedAt(x: Int) = x % 2 == 0

      //What we do if this does partial function matches
      def apply(v1: Int) = v1 * 2
    }

val tripleOdds: PartialFunction[Int, Int] = {
      case x: Int if (x % 2) != 0 => x * 3				// syntaxic sugar (usual way)
    }

val whatToDo = doubleEvens orElse tripleOdds 			//	combine the partial functions together: OrElse

val addFive = (x: Int) => x + 5
val whatToDo = doubleEvens orElse tripleOdds andThen addFive  // chain (partial) functions together: andThen
```

## Classes, Objects, and Traits

```scala
class C(x: R)	                    // constructor params - x is only available in class body
class C(val x: R) 					// c.x	constructor params - automatic public (immutable) member defined
class D(var x: R)   				// you can define class with var or val parameters

class C(var x: R) {
  assert(x > 0, "positive please")  // constructor is class body
  var y = x                         // declare a public member
  val readonly = 5                  // declare a gettable but not settable member
  private var secret = 1            // declare a private member
  def this = this(42)               // alternative constructor
}

new{ ... }	// anonymous class
abstract class D { ... }	// define an abstract(non-createable) class.
class C extends D { ... }	// define an inherited class. Class hierarchy is linear, a class can only extend from one parent class
class C(x: R) extends D(x)	// inheritance and constructor params. (wishlist: automatically pass-up params by default)
// A class can be placed inside another class
object O extends D { ... }	// define a singleton.

trait T { ... } 			// traits. See below.
class C extends T { ... }
class C extends D with T { ... }

// interfaces-with-implementation. no constructor params. mixin-able.
trait T1; trait T2
class C extends T1 with T2          // multiple traits.
class C extends D with T1 with T2	// parent class and (multiple) trait(s).
class C extends D { override def f = ...}	// must declare method overrides.

var c = new C(4)		// Instantiation
//BAD new List[Int]
//GOOD List(1,2,3)		// Instead, convention: callable factory shadowing the type

classOf[String]	// class literal.
classOf[String].getCanonicalName
classOf[String].getSimpleName
val zoom = "zoom"
zoom.getClass == classOf[String]

x.isInstanceOf[String]	// type check (runtime)
x.asInstanceOf[String]	// type cast (runtime)
x: String				// compare to parameter ascription (compile time)
```

### Methods

```scala
class Complex(real: Double, imaginary: Double) {
    def re = real       // return type inferred automatically by the compiler
    def im = imaginary  // methods without arguments
    def print(): Unit = println(s"$real + i * $imaginary")
	override def toString() = "" + re + (if (im < 0) "" else "+") + im + "i"  // override methods inherited from a super-class
}
```

### Asserts and Contracts

Asserts take a boolean argument and can take a message.

```scala
assert(true) // should be true
assert(true, "This should be true")
```

```scala
def addNaturals(nats: List[Int]): Int = {
  require(nats forall (_ >= 0), "List contains negative numbers")
  nats.foldLeft(0)(_ + _)
} ensuring(_ >= 0)
```

### Path-dependent Classes

When a class is instantiated inside of another object, it belongs to the instance.  This is a path dependent type. Once established, it cannot be placed inside of another object

```scala
case class Board(length: Int, height: Int) {
  case class Coordinate(x: Int, y: Int)
}

val b1 = Board(20, 20)
val b2 = Board(30, 30)
val c1 = b1.Coordinate(15, 15)
val c2 = b2.Coordinate(25, 25)
// val c1 = c2  won't work
```

Use ``A#B`` for a Java-style inner class:

```scala
class Graph {
  class Node {
    var connectedNodes: List[Graph#Node] = Nil			// accepts Nodes from any Graph
    def connectTo(node: Graph#Node) {
      if (connectedNodes.find(node.equals).isEmpty) {
        connectedNodes = node :: connectedNodes
      }
    }
  }
  var nodes: List[Node] = Nil
  def newNode: Node = {
    val res = new Node
    nodes = res :: nodes
    res
  }
}
```

### Companion Objects

Static members (methods or fields) do not exist in Scala. Rather than defining static members, the Scala programmer declares these members in singleton objects, that is a class with a single instance.

```scala
object TimerAnonymous {
    def oncePerSecond(callback: () => Unit) {
        while (true) { callback(); Thread sleep 1000 }
    }
    def main(args: Array[String]) {
        oncePerSecond(() => println("time flies like an arrow..."))
    }
}
```

- An object that has the same name as class is called a companion object, it is used to contain factories for the class that it complements.
- A companion object can also store shared variables and values for every instantiated class to share.
- A companion object can see private values and variables of the instantiated object

### Apply Method

The apply method is a magical method in Scala.

```scala
class Employee (val firstName:String, val lastName:String)

object Employee {
	def apply(firstName:String, lastName:String) = new Employee(firstName, lastName)  // would also work in a class, but rarer
}

val a = Employee("John", "Doe")
// is equivalent to
var b = Employee.apply("John", "Doe")
```

## Case Classes

- The ``new`` keyword is not mandatory to create instances of these classes (i.e. one can write Const(5) instead of new Const(5)),
- Getter functions are automatically defined for the constructor parameters (i.e. it is possible to get the value of the v constructor parameter of some instance c of class Const just by writing c.v),
- Default definitions for methods equals and hashCode are provided, which work on the structure of the instances and not on their identity,
- A default definition for method toString is provided, and prints the value in a source form (e.g. the tree for expression x+1 prints as Sum(Var(x),Const(1))),
- Instances of these classes can be decomposed through pattern matching

```scala
case class Person(first: String, last: String, age: Int = 0)  // Case classes can have default and named parameters
val p1 = Person("Fred", "Jones")    // new is optional
val p2 = new Person("Fred", "Jones")
p1 == p2  							// true
p1.hashCode == p2.hashCode  		// true
p1 eq p2  							// false
val p3 = p2.copy(first = "Jane") 	// copy the case class but change the name in the copy
```

```scala
case class Dog(var name: String, breed: String)  	// Case classes can have mutable properties - potentially unsafe
```

Case classes can be disassembled to their constituent parts as a tuple:

```scala
val parts = Person.unapply(p1).get // returns Option[T]
parts._1
parts._2
```

### Algebraic data type

```scala
sealed trait Tree    // or abstract class
final case class Sum(l: Tree, r: Tree) extends Tree
final case class Var(n: String) extends Tree
final case class Const(v: Int) extends Tree
```

### Pattern Matching

``{ case "x" => 5 }`` defines a partial function which, when given the string "x" as argument, returns the integer 5, and fails with an exception otherwise.

```scala
type Environment = String => Int  // the type Environment can be used as an alias of the type of functions from String to Int

def eval(t: Tree, env: Environment): Int = t match {
    case Sum(l, r) => eval(l, env) + eval(r, env)
    case Var(n) => env(n)
    case Const(v) => v
}

def derive(t: Tree, v: String): Tree = t match {
    case Sum(l, r) => Sum(derive(l, v), derive(r, v))
    case Var(n) if (v == n) => Const(1)                  // guard, an expression following the if keyword.
    case _ => Const(0)                                   // wild-card, written _, which is a pattern matching any value, without giving it a name.
}
```

```scala
// GOOD (xs zip ys) map { case (x,y) => x*y }
// BAD (xs zip ys) map( (x,y) => x*y )	// use case in function args for pattern matching.
// BAD
val v42 = 42
Some(3) match {
  case Some(v42) => println("42")
  case _ => println("Not 42")
}	// “v42” is interpreted as a name matching any Int value, and “42” is printed.
// GOOD
val v42 = 42
Some(3) match {
  case Some(`v42`) => println("42")
  case _ => println("Not 42")
}	// ”`v42`” with backticks is interpreted as the existing val v42, and “Not 42” is printed.
// GOOD
val UppercaseVal = 42
Some(3) match {
  case Some(UppercaseVal) => println("42")
  case _ => println("Not 42")
}	// UppercaseVal is treated as an existing val, rather than a new pattern variable, because it starts with an uppercase letter.
// Thus, the value contained within UppercaseVal is checked against 3, and “Not 42” is printed.
```

### List Matching

```scala
val secondElement = List(1,2,3) match {
      case x :: y :: xs => xs
	  case x :: Nil => x
      case _ => 0
    }
```

### Regex

```scala
val MyRegularExpression = """a=([^,]+),\s+b=(.+)""".r  			//.r turns a String to a regular expression
expr match {
      case (MyRegularExpression(a, b)) => a + b
	  }
```

```scala
import scala.util.matching.Regex

val numberPattern: Regex = "[0-9]".r

numberPattern.findFirstMatchIn("awesomepassword") match {
  case Some(_) => println("Password OK")
  case None => println("Password must contain a number")
}
```

With groups:

```scala
val keyValPattern: Regex = "([0-9a-zA-Z-#() ]+): ([0-9a-zA-Z-#() ]+)".r

for (patternMatch <- keyValPattern.findAllMatchIn(input))
  println(s"key: ${patternMatch.group(1)} value: ${patternMatch.group(2)}")
```

### Extractors (unapply)

```scala
class Car(val make: String, val model: String, val year: Short, val topSpeed: Short)

object Car {    													// What is typical is to create a custom extractor in the companion object of the class.
  def unapply(x: Car) = Some(x.make, x.model, x.year, x.topSpeed)   // returns an Option[T]
}

val Car(a, b, c, d) = new Car("Chevy", "Camaro", 1978, 120)  	// assign values to a .. d

val x = new Car("Chevy", "Camaro", 1978, 120) match { 			// pattern matching
  case Car(s, t, _, _) => (s, t) 								// _ for variables we don't care about.
  case _ => ("Ford", "Edsel")  									// fallback
}
```

- As long as the method signatures aren't the same, you can have an many unapply methods as you want in the same class / object.
- When you create a case class, it automatically can be used with pattern matching since it has an extractor.


### Value Class

Avoid allocating runtime objects.

```scala
class Wrapper(val underlying: Int) extends AnyVal {
  def foo: Wrapper = new Wrapper(underlying * 19)
}
```
It has a single, public val parameter that is the underlying runtime representation. The type at compile time is Wrapper, but at runtime, the representation is an Int. A value class can define defs, but no vals, vars, or nested traitss, classes or objects

A value class can only extend universal traits and cannot be extended itself. A universal trait is a trait that extends Any, only has defs as members, and does no initialization. Universal traits allow basic inheritance of methods for value classes, but they incur the overhead of allocation.

## Traits

Apart from inheriting code from a super-class, a Scala class can also import code from one or several traits i.e. interfaces which can also contain code.
In Scala, when a class inherits from a trait, it implements that traits's interface, and inherits all the code contained in the trait.

```scala
trait Ord {
    def < (that: Any): Boolean                              // The type Any which is used above is the type which is a super-type of all other types in Scala
    def <=(that: Any): Boolean = (this < that) || (this == that)
    def > (that: Any): Boolean = !(this <= that)
    def >=(that: Any): Boolean = !(this < that)
}

class Date(y: Int, m: Int, d: Int) extends Ord {
    def year = y
    def month = m
    def day = d
    override def toString(): String = year + "-" + month + "-" + day

    override def equals(that: Any): Boolean =
        that.isInstanceOf[Date] && {
        val o = that.asInstanceOf[Date]
        o.day == day && o.month == month && o.year == year
    }

    def <(that: Any): Boolean = {    // The trait declare the type (e.g. method), where a concrete implementer will satisfy the type
        if (!that.isInstanceOf[Date])
            error("cannot compare " + that + " and a Date")
        val o = that.asInstanceOf[Date](year < o.year) ||
            (year == o.year && (month < o.month ||
            (month == o.month && day < o.day    )))
    }
}
```

- Traits can have concrete implementations that can be mixed into concrete classes with its own state

- Traits can be mixed in during instantiation!

```scala
trait Logging {
      var logCache = List[String]()

      def log(value: String) = {
        logCache = logCache :+ value
      }

      def log = logCache
    }
val a = new A("stuff") with Logging  // mixin traits during instantiation!
a.log("I did something")
a.log.size
```

### Stackable Traits

```scala
abstract class IntQueue {
  def get(): Int
  def put(x: Int)
}

import scala.collection.mutable.ArrayBuffer

class BasicIntQueue extends IntQueue {
  private val buf = new ArrayBuffer[Int]
  def get() = buf.remove(0)
  def put(x: Int) { buf += x }
}

trait Doubling extends IntQueue {
  abstract override def put(x: Int) { super.put(2 * x) }    // abstract override is necessary to stack traits
}

class MyQueue extends BasicIntQueue with Doubling			// could also mixin during instantiation

val myQueue = new MyQueue
myQueue.put(3)
myQueue.get()
```

- More traits can be stacked one atop another, make sure that all overrides are labelled ``abstract override``.
- The order of the mixins are important. Traits on the right take effect first.
- Traits are instantiated before a classes instantiation from left to right.
- Linerization: the diamond inheritance problem is avoided since instantiations are tracked and will not allow multiple instantiations of the same parent trait

### Classes versus Traits

Use classes:

- When a behavior is not going to be reused at all or in multiple places
- When you plan to use your Scala code from another language, for example, if you are building a library that could be used in Java

Use traits:

- When a behavior is going to be reused in multiple unrelated classes.
- When you want to define interfaces and want to use them outside Scala, for example Java. The reason is that the traits that do not have any implementations are compiled similar to interfaces.


## Keyword List

    abstract
    case
    catch
    class
    def
    do
    else
    extends
    false
    final
    finally
    for
    forSome
    if
    implicit
    import
    lazy
    match
    new
    Null
    object
    override
    package
    private
    protected
    return
    sealed
    super
    this
    throw
    trait
    Try
    true
    type
    val
    var
    while
    with
    yield
     -
     :
     =
     =>
    <-
    <:
    <%
    >:
    #
    @