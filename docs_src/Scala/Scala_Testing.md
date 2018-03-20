---
title: Scala Testing
category: Scala
tags: Scala, Tests
---

## Links

[http://www.scalatest.org/](http://www.scalatest.org/)

[Writing TDD unit tests with scalatest](https://alvinalexander.com/scala/writing-tdd-unit-tests-with-scalatest)

[At a Glance](http://www.scalatest.org/at_a_glance/)


## Examples

```scala
libraryDependencies += "org.scalatest" %% "scalatest" % "2.2.6" % "test"
```

```scala
package com.acme.pizza

import org.scalatest.FunSuite
import org.scalatest.BeforeAndAfter

class PizzaTests extends FunSuite with BeforeAndAfter {
  
  var pizza: Pizza = _

  before {
    pizza = new Pizza
  }

  test("new pizza has zero toppings") {
    assert(pizza.getToppings.size == 0)
  }

  test("adding one topping") {
    pizza.addTopping(Topping("green olives"))
    assert(pizza.getToppings.size === 1)
  }

  // mark that you want a test here in the future
  test ("test pizza pricing") (pending)

}
```

## [Styles](http://www.scalatest.org/at_a_glance/)

### FunSuite

```scala
import org.scalatest.FunSuite 
class AddSuite extends FunSuite {    
  test("3 plus 3 is 6") {      
     assert((3 + 3) == 6)    
  }  
}
```

### FlatSpec

The structure of this test is flat—like xUnit, but the test name can be written in specification style:
	
```scala
import org.scalatest.FlatSpec  
class AddSpec extends FlatSpec {  
  "Addition of 3 and 3" should "have result 6" in { 
    assert((3 + 3) == 0)    
  }  
}
```

```scala
import collection.mutable.Stack
import org.scalatest._

class ExampleSpec extends FlatSpec with Matchers {

  "A Stack" should "pop values in last-in-first-out order" in {
    val stack = new Stack[Int]
    stack.push(1)
    stack.push(2)
    stack.pop() should be (2)
    stack.pop() should be (1)
  }

  it should "throw NoSuchElementException if an empty stack is popped" in {
    val emptyStack = new Stack[Int]
    a [NoSuchElementException] should be thrownBy {
      emptyStack.pop()
    } 
  }
}
```	

### FeatureSpec

```scala
import org.scalatest._  

class Calculator {    
  def add(a:Int, b:Int): Int = a + b 
} 
  
class CalcSpec extends FeatureSpec with GivenWhenThen {
  info("As a calculator owner")    
  info("I want to be able add two numbers")    
  info("so I can get a correct result")    
  feature("Addition") {
    scenario("User adds two numbers") {
      Given("a calculator")        
      val calc = new Calculator 
      When("two numbers are added")        
      var result = calc.add(3, 3) 
      Then("we get correct result")        
       assert(result == 6)      
    }
  }  
} 
```
