
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


## Syntax

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


## Compilation

```shell
scalac HelloWorld.scala  // produces HelloWorld.class
scala -classpath . HelloWorld
```


## Variables and Values

```scala
var x = 5 // variable
val x = 5 // "const"
var x: Double = 5 // explicit type
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


## Imports

All classes from the java.lang package are imported by default, while others need to be imported explicitly.

```
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

### Anonymous Functions

```
object TimerAnonymous {
    def oncePerSecond(callback: () => Unit) {
        while (true) { callback(); Thread sleep 1000 }
    }
    def main(args: Array[String]) {
        oncePerSecond(() => println("time flies like an arrow..."))
    }
}
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
class Reference[T] {
    private var contents: T = _             // _ represents a default value. This default value is 0 for numeric types, false for the Boolean type, () for the Unit type and null for all object types.
    def set(value: T) { contents = value }
    def get: T = contents
}
```


## Frameworks

- The Lift Framework
- The Play framework
- The Bowler framework
- Akka