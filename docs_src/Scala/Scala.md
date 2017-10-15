
## Links

- [Scala Cheatsheet]( http://docs.scala-lang.org/cheatsheets/ )
- [Scala @ TutorialPoint]( https://www.tutorialspoint.com/scala/index.htm )
- [Scala Tutorial (PDF)]( http://www.scala-lang.org/docu/files/ScalaTutorial.pdf )


## Main Features of Scala

- All types are objects
- Type inference
- Nested Functions
- Functions are objects
- Domain specific language (DSL) support
- Traits
- Closures
- Concurrency support inspired by Erlang


## Style

Class Names - For all class names, the first letter should be in Upper Case. If several words are used to form a name of the class, each inner word's first letter should be in Upper Case.

``class MyFirstScalaClass``

Method Names - All method names should start with a Lower Case letter. If multiple words are used to form the name of the method, then each inner word's first letter should be in Upper Case.

``def myMethodName()``

Program File Name - Name of the program file should exactly match the object name. When saving the file you should save it using the object name (Remember Scala is case-sensitive) and append ".scala" to the end of the name. If the file name and the object name do not match your program will not compile.

Assume 'HelloWorld' is the object name: the file should be saved as 'HelloWorld.scala'.


## Keywords

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

## Tools

REPL http://ammonite.io/#ScalaScripts

https://scalafiddle.io/

  
### Install

* Need to have Java Software Development Kit (SDK) installed 

```
java --version
```

```shell
export JAVA_HOME=/usr/local/java-current
export PATH=$PATH:$JAVA_HOME/bin/
```

http://www.scala-lang.org/download/

### Compilation

```shell
scalac HelloWorld.scala  // produces HelloWorld.class
scala -classpath . HelloWorld
```

# Language

## Variables and Values

```scala
var x = 5 // variable
val x = 5 // immutable value / "const" 
var x: Double = 5 // explicit type
println(x)
```


## Entry Point

```scala
object HelloWorld {
    def main(args: Array[String]) {
        println("Hello, world!")
    }
}
```

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

## Imports

All classes from the java.lang package are imported by default. The Predef object provides definitions that are accessible in all Scala compilation units without explicit qualification:
- immutable Map, Set, List, ::, Nil, print, println, assert, assume, require, ensuring

```scala
import scala.collection.mutable.HashMap

import java.util.{Date, Locale}  // Multiple classes can be imported from the same package by enclosing them in curly braces
import java.text.DateFormat
import java.text.DateFormat._    // When importing all the names of a package or class, one uses the underscore character (_) instead of the asterisk (*). 

object FrenchDate {
    def main(args: Array[String]) {
        val now = new Date
        val df = getDateInstance(LONG, Locale.FRANCE)
    println(df format now)       // Methods taking one argument can be used with an infix syntax. Equivalent to df.format(now)   
    }
}
```

```scala
import scala.collection._	// wildcard import.
import scala.collection.Vector 
import scala.collection.{Vector, Sequence}	// selective import.
import scala.collection.{Vector => Vec28}	// renaming import.
import java.util.{Date => _, _}	                // import all from java.util except Date.
```

## Packages

```scala
package pkg 		// at start of file 
package pkg { ... }	// declare a package.
``` 

## Expressions

You can combine expressions by surrounding them with {}. We call this a block.
The result of the last expression in the block is the result of the overall block, too.

```scala
println({
  val x = 1 + 1
  x + 1
}) // 3
```

## Data Structures

```scala
import scala.collection.mutable.HashMap
import scala.collection.immutable.{TreeMap, TreeSet}
```

```scala
(1,2,3)	// tuple literal. (Tuple3)
var (x,y,z) = (1,2,3)	// destructuring bind: tuple unpacking via pattern matching.
BADvar x,y,z = (1,2,3)	// hidden error: each assigned to the entire tuple.
var xs = List(1,2,3)	// list (immutable).
xs(2)	        // paren indexing
1 :: List(2,3)	// cons.
1 to 5          // same as 1 until 6 
1 to 10 by 2	// range sugar.
() // (empty parens)	sole member of the Unit type (like C/Java void).
```

### Control constructs

```scala
if (check) happy else sad	// conditional.
if (check) happy                // same as 
if (check) happy else ()	// conditional sugar.
while (x < 5) { println(x); x += 1}	// while loop.
do { println(x); x += 1} while (x < 5)	// do while loop.
import scala.util.control.Breaks._
breakable {
for (x <- xs) {
if (Math.random < 0.1) break
}
}	break. (slides)
for (x <- xs if x%2 == 0) yield x*10 // same as 
xs.filter(_%2 == 0).map(_*10)	     // for comprehension: filter/map
for ((x,y) <- xs zip ys) yield x*y   // same as 
(xs zip ys) map { case (x,y) => x*y }	// for comprehension: destructuring bind
for (x <- xs; y <- ys) yield x*y     // same as 
xs flatMap {x => ys map {y => x*y}}  // for comprehension: cross product
for (x <- xs; y <- ys) {
println("%d/%d = %.1f".format(x, y, x/y.toFloat))
}	// for comprehension: imperative-ish
// sprintf-style
for (i <- 1 to 5) {
println(i)
}	// for comprehension: iterate including the upper bound
for (i <- 1 until 5) {
println(i)
}	// for comprehension: iterate omitting the upper bound
```

## Object Orientation
 
```scala
class C(x: R)	constructor params - x is only available in class body
class C(val x: R)
var c = new C(4)
c.x	constructor params - automatic public member defined
class C(var x: R) {
assert(x > 0, "positive please")
var y = x
val readonly = 5
private var secret = 1
def this = this(42)
}	
// constructor is class body
// declare a public member
// declare a gettable but not settable member
// declare a private member
// alternative constructor
new{ ... }	// anonymous class
abstract class D { ... }	// define an abstract class. (non-createable)
class C extends D { ... }	// define an inherited class.
class D(var x: R)
class C(x: R) extends D(x)	// inheritance and constructor params. (wishlist: automatically pass-up params by default)
object O extends D { ... }	// define a singleton. (module-like)
trait T { ... }
class C extends T { ... }
class C extends D with T { ... }	// traits.
// interfaces-with-implementation. no constructor params. mixin-able.
trait T1; trait T2
class C extends T1 with T2
class C extends D with T1 with T2	// multiple traits.
class C extends D { override def f = ...}	// must declare method overrides.
new java.io.File("f")	// create object.
//BAD new List[Int]
//GOOD List(1,2,3)	type error: abstract type
//instead, convention: callable factory shadowing the type
classOf[String]	// class literal.
x.isInstanceOf[String]	// type check (runtime)
x.asInstanceOf[String]	// type cast (runtime)
x: String	// ascription (compile time)
```

```scala
class Greeter(prefix: String, suffix: String) {
  def greet(name: String): Unit =
    println(prefix + name + suffix)
}
```

## Scala is Object-Oriented

Scala is a pure object-oriented language in the sense that everything is an object, including numbers or functions. 

``1 + 2 * 3 / x`` consists exclusively of method calls, because it is equivalent to the following expression: ``(1).+(((2).*(3))./(x))``
This also means that +, *, etc. are valid identifiers in Scala.

Types and behavior of objects are described by classes and traits.

Classes are extended by subclassing and a flexible mixin-based composition mechanism as a clean replacement for multiple inheritance.

```scala
class Complex(real: Double, imaginary: Double) {
    def re = real       // return type inferred automatically by the compiler  
    def im = imaginary  // methods withot arguments
    override def toString() = "" + re + (if (im < 0) "" else "+") + im + "i"  // override methods inherited from a super-class
}
```

## Scala is Functional

Scala is also a functional language in the sense that every function is a value and every value is an object so ultimately every function is an object.
Scala provides a lightweight syntax for defining anonymous functions, it supports higher-order functions, it allows functions to be nested, and supports currying. 

```scala
object Timer {
    def oncePerSecond(callback: () => Unit) {
        while (true) { callback(); Thread sleep 1000 }
    }
    
    def timeFlies() {
        println("time flies like an arrow...")
    }
    
    def main(args: Array[String]) {
        oncePerSecond(timeFlies)
    }
}
```


## Functions and Methods

```scala
val add = (x: Int, y: Int) => x + y // anonymous function

def add(x: Int, y: Int): Int = x + y  // method - the return type is declared after the parameter list and a colon

// GOOD def f(x: Any) = println(x)
// BAD def f(x) = println(x)	// syntax error: need types for every arg.

def f(x: Int) = { 
  val square = x*x
  square.toString 
  } // The last expression in the body is the method’s return value. (Scala does have a return keyword, but it’s rarely used.)

// BAD def f(x: Int) { x*x }  hidden error: without = it’s a Unit-returning procedure; causes havoc

// Methods can take multiple parameter lists or none at all
def addThenMultiply(x: Int, y: Int)(multiplier: Int): Int = (x + y) * multiplier
def name: String = System.getProperty("name")
```

```scala
type R = Double	// type alias
def f(x: R)     // vs.
// call-by-name (lazy parameters)
```

```scala
(1 to 5).map(_*2)
(1 to 5).reduceLeft( _+_ ) // anonymous function: underscore is positionally matched arg.
(1 to 5).map( x => x*x ) 
(1 to 5).map { x => val y=x*2; println(y); y }  // anonymous function: block style returns last expression.
(1 to 5) filter {_%2 == 0} map {_*2} // pipeline style
(x:R) => x*x	// anonymous function
(1 to 5).map(_*2) // vs.
(1 to 5).reduceLeft( _+_ )	// anonymous function: underscore is positionally matched arg.
(1 to 5).map( x => x*x )	// anonymous function: to use an arg twice, have to name it.
// GOOD (1 to 5).map(2*)
// BAD (1 to 5).map(*2)	                        // anonymous function: bound infix method. Use 2*_ for sanity’s sake instead.
(1 to 5).map { x => val y=x*2; println(y); y }	// anonymous function: block style returns last expression.
(1 to 5) filter {_%2 == 0} map {_*2}	        // anonymous functions: pipeline style. (or parens too).
def compose(g:R=>R, h:R=>R) = (x:R) => g(h(x)) 
val f = compose({_*2}, {_-1})	// anonymous functions: to pass in multiple blocks, need outer parens.
val zscore = (mean:R, sd:R) => (x:R) => (x-mean)/sd	// currying, obvious syntax.
def zscore(mean:R, sd:R) = (x:R) => (x-mean)/sd	        // currying, obvious syntax
def zscore(mean:R, sd:R)(x:R) = (x-mean)/sd	        // currying, sugar syntax. but then:
val normer = zscore(7, 0.4) _	                        // need trailing underscore to get the partial, only for the sugar version.
def mapmake[T](g:T=>T)(seq: List[T]) = seq.map(g)	// generic type.
5.+(3); 5 + 3 
(1 to 5) map (_*2)	// infix sugar.
def sum(args: Int*) = args.reduceLeft(_+_)	// varargs.
```

## Contracts

```scala
def addNaturals(nats: List[Int]): Int = {
  require(nats forall (_ >= 0), "List contains negative numbers")
  nats.foldLeft(0)(_ + _)
} ensuring(_ >= 0)
```

### Anonymous Functions

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


### Variable Length Arguments

There is a special syntax for methods that can take parameters of a repeated type. To apply String’s capitalize function to several strings, you might write:

```scala
def capitalizeAll(args: String*) = {
      args.map { arg =>
        arg.capitalize
      }
    }

//    scala> capitalizeAll("rarity", "applejack")
```    


### Partial Applications

```shell
scala> def adder(m: Int, n: Int) = m + n
adder: (m: Int,n: Int)Int
scala> val add2 = adder(2, _:Int)
add2: (Int) => Int = <function1>

scala> add2(3)
res50: Int = 5
```

You can partially apply any argument in the argument list, not just the last one.

### Types

```scala
type R = Double // type alias
```



## Case Classes

```scala
abstract class Tree
case class Sum(l: Tree, r: Tree) extends Tree
case class Var(n: String) extends Tree
case class Const(v: Int) extends Tree
```

- The ``new`` keyword is not mandatory to create instances of these classes (i.e. one can write Const(5) instead of new Const(5)),
- Getter functions are automatically defined for the constructor parameters (i.e. it is possible to get the value of the v constructor parameter of some instance c of class Const just by writing c.v),
- Default definitions for methods equals and hashCode are provided, which work on the structure of the instances and not on their identity,
- A default definition for method toString is provided, and prints the value in a source form (e.g. the tree for expression x+1 prints as Sum(Var(x),Const(1))),
- Instances of these classes can be decomposed through pattern matching


## Pattern Matching

``{ case "x" => 5 }`` defines a function which, when given the string "x" as argument, returns the integer 5, and fails with an exception otherwise.

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
// BAD (xs zip ys) map( (x,y) => x*y )	use case in function args for pattern matching.
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



## Traits

Apart from inheriting code from a super-class, a Scala class can also import code from one or several traits i.e. interfaces which can also contain code. 
In Scala, when a class inherits from a trait, it implements that traits's interface, and inherits all the code contained in the trait.

```scala
trait Ord {
    def < (that: Any): Boolean                                   // The type Any which is used above is the type which is a super-type of all other types in Scala
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
    
    def <(that: Any): Boolean = {
        if (!that.isInstanceOf[Date])
            error("cannot compare " + that + " and a Date")
        val o = that.asInstanceOf[Date](year < o.year) ||
            (year == o.year && (month < o.month ||
            (month == o.month && day < o.day    )))
    }
    
}
```


## Generics

```scala
trait Cache[K, V] {
      def get(key: K): V
      def put(key: K, value: V)
      def delete(key: K)
    }
    
def remove[K](key: K)
```

```scala
class Reference[T] {
    private var contents: T = _             // _ represents a default value. This default value is 0 for numeric types, false for the Boolean type, () for the Unit type and null for all object types.
    def set(value: T) { contents = value }
    def get: T = contents
}
```


## Root Package

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


## Frameworks

- [The Lift Framework]( https://liftweb.net/ )
- [The Play framework]( https://www.playframework.com/ )
- [The Bowler framework]( https://github.com/bowler-framework/bowler-quickstart )
- [Akka]( http://akka.io/ )
