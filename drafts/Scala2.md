

https://gist.github.com/arosien/0aee59cc734042f7044d24bdaec731a8

## Algebraic Data Types



```scala
// A website visitor is: logged in; or anonymous
// A logged in user has:
//   an ID; and
//   an email address

sealed trait Visitor {
  def fold[B](
    ifLoggedIn: (Long, String) => B,
    ifAnonymous: () => B): B =
    this match {
      case LoggedIn(id, email) =>
        ifLoggedIn(id, email)
      case Anonymous() =>
        ifAnonymous()
    }

  // how de we write toJson using fold?
  def toJson2(): String =
    fold(
      (id, email) => s"{type:logged_in,id:$id, email:$email}",
      () => "{type:anonymous}")

  def toJson(): String =
    this match {
      case LoggedIn(id, email) => s"{type:logged_in,id:$id, email:$email}"
      case Anonymous() => "{type:anonymous}"
    }
}
case class LoggedIn(id: Long, email: String) extends Visitor
case class Anonymous() extends Visitor
```

## Structural Recursion

Goal: transform algebraic data types
Structure of the code follows structure of the data
Two (sub-)patterns: pattern matching and polymorphism

Summary

Processing algebraic data types immediately follows from the structure of the data
Can choose between pattern matching and polymorphism
Pattern matching (within the base trait) is usually preferred


// Calculation.add(value: Int): Calculation

```scala
// A calculation is a success or failure
// A success has a value.
// A failure has an error
sealed trait Calculation {
  def add(value: Int): Calculation =
    this match {
      case Success(v) => Success(v + value)
      case f @ Failure(msg) => f
    }

  def failLoudly(): Calculation =
    this match {
      case s: Success => s
      case Failure(msg) => Failure(msg + "!!!")
    }
}
case class Success(value: Int) extends Calculation
case class Failure(msg: String) extends Calculation

val calc = Success(12) // constructor
```

```scala
sealed trait MyList[A] {
  def fold[B](
    ifEmpty: () => B,
    ifPair: (A, B) => B): B =
    this match {
      case Empty() =>
        ifEmpty()
      case Pair(head, tail) =>
        ifPair(
          head, // A
          tail.fold(ifEmpty, f)) // B
    }
}
case class Empty[A]() extends MyList[A]
case class Pair[A](head: A, tail: MyList[A]) extends MyList[A]
```

## Sequencing Computation

Goal: patterns for sequencing computations
Functional programming is about transforming values
That is all you can do without introducing side-effects
A => B => C
This is sequencing computations
Three patterns: fold, map, and flatMap
fold
A => B
Abstraction over structural recursion
-> Convert user to JSON

map
F[A] => (A => B) => F[B]
-> Get user from database (might not be a user): Result[User] -> Get order for user (might not be an order): User => Result[Order]

flatMap
F[A] => (A => F[B]) => F[B]
-> Get user by id: UserId => Result[User] -> Get user’s order: User => Result[Order] -> Transform order to JSON: (Order => Json) => Result[Json] -> Send JSON: Result[Json] => Response

Summary
Standard patterns for sequencing computations
fold is general transformation for algebraic data types
map: F[A] => (A => B) => F[B]
flatMap: F[A] => (A => F[B]) => F[B]
You can teach monads in an introductory course!

// fold: A => B


// Convert user to JSON


// A Result is a Success with value A or a Failure (with no value)
sealed trait Result[A] {
  def map[B](f: A => B): Result[B] =
    this match {
      case Success(a) => Success(f(a))
      case f: Failure => f
    }
}
case class Success[A](value: A) extends Result[A]
case class Failure[A]() extends Result[A]


// map: F[A] => (A => B) => F[B]


// Get user from database (might not be a user): Result[User]
def getUser(id: Long): Result[User]
// Get order for user (might not be an order): User => Result[Order]
def getOrder(user: User): Result[Order]

val order: Result[Order] =
  getUser(12) // Result[User]
    .flatMap(getOrder) // User => Result[Order]


// flatMap: F[A] => (A => F[B]) => F[B]


// Get user by id: UserId => Result[User]
// Get user's order: User => Result[Order]
// Transform order to JSON: (Order => Json) => Result[Json]
// Send JSON: Result[Json] => Response
 

 
 