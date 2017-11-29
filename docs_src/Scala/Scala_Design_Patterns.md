---
title: Scala Design Patterns
category: Scala
tags: Scala, Design Patterns
---


## Static Factory

```scala
trait Animal
class Bird extends Animal
class Mammal extends Animal
class Fish extends Animal

object Animal {
  def apply(animal: String): Animal = animal.toLowerCase match {
    case "bird" => new Bird
    case "mammal" => new Mammal
    case "fish" => new Fish
    case x: String => throw new RuntimeException(s"Unknown animal: $x")
  }
}
```

## Algebraic Data Types and Pattern Matching

```scala
sealed trait Shape 
case class Circle(radius: Double) extends Shape 
case class Rectangle(height: Double, width: Double) extends Shape

object Shape { 
  def area(shape: Shape): Double = 
    shape match { 
      case Circle(Point(x, y), radius) => Math.PI * Math.pow(radius, 2) 
      case Rectangle(_, h, w) => h * w 
    } 
}
```

They have only data and do not contain any functionality on top of this data as normal classes would. 

## Stackable Traits

```scala
abstract class StringWriter {
  def write(data: String): String
}

class BasicStringWriter extends StringWriter {
  override def write(data: String): String =
    s"Writing the following data: ${data}"
}

trait CapitalizingStringWriter extends StringWriter {
  abstract override def write(data: String): String = {
    super.write(data.split("\\s+").map(_.capitalize).mkString(" "))
  }
}

trait UppercasingStringWriter extends StringWriter {
  abstract override def write(data: String): String = {
    super.write(data.toUpperCase)
  }
}

object Example {
  def main(args: Array[String]): Unit = {
    val writer1 = new BasicStringWriter with UppercasingStringWriter with CapitalizingStringWriter
    System.out.println(s"Writer 1: '${writer1.write("we like learning scala!")}'")
  }
}
```

_Stackable traits order of execution_

Stackable traits are always executed from the right mixin to the left. 
Sometimes, however, if we only get output and it doesn't depend on what is passed to the method, we simply end up with method calls on a stack, which then get evaluated and it will appear as if things are applied from left to right.

## Components / Cake Pattern

[http://jonasboner.com/real-world-scala-dependency-injection-di/](http://jonasboner.com/real-world-scala-dependency-injection-di/)

```scala
// Service Interfaces and Component Definitions

trait OnOffDeviceComponent {
  val onOff: OnOffDevice  // abstract val
  
  trait OnOffDevice {
    def on: Unit
    def off: Unit
  }
}

trait SensorDeviceComponent {
  val sensor: SensorDevice
  
  trait SensorDevice {
    def isCoffeePresent: Boolean
  }
}

// =======================
// Component / Service Implementations

trait OnOffDeviceComponentImpl extends OnOffDeviceComponent {
  class Heater extends OnOffDevice {
    def on = println("heater.on")
    def off = println("heater.off")
  }
}

trait SensorDeviceComponentImpl extends SensorDeviceComponent {
  class PotSensor extends SensorDevice {
    def isCoffeePresent = true
  }
}

// =======================
// Component declaring two dependencies that it wants injected
trait WarmerComponentImpl {
  this: SensorDeviceComponent with OnOffDeviceComponent =>     // Use of self-type for composition
  class Warmer {
    def trigger = {
      if (sensor.isCoffeePresent) onOff.on
      else onOff.off
    }
  }
}

// =======================
// Instantiation (and configuration) of the services in the ComponentRegistry module 

object ComponentRegistry extends
  OnOffDeviceComponentImpl with
  SensorDeviceComponentImpl with
  WarmerComponentImpl {

  val onOff = new Heater      // all instantiations in one spot; can be easily be replaced by e.g. mocks 
  val sensor = new PotSensor
  val warmer = new Warmer
}

// =======================
val warmer = ComponentRegistry.warmer
warmer.trigger

```


## Type Classes (using context-bound type parameters)

```scala
// Define some behavior in terms of operations that a type must support in order to be considered a member of the type class.
trait Number[T] {
  def plus(x: T, y: T): T
  def divide(x: T, y: Int): T
}

// Define the default type class members in the companion object of the trait
object Number {

  implicit object DoubleNumber extends Number[Double] {
    override def plus(x: Double, y: Double): Double = x + y
    override def divide(x: Double, y: Int): Double = x / y
  }
} 
 
object Stats {

//  same as
//  def mean[T](xs: Vector[T])(implicit ev: Number[T]): T =
//    ev.divide(xs.reduce(ev.plus(_, _)), xs.size)
  
  def mean[T: Number](xs: Vector[T]): T = 
    implicitly[Number[T]].divide(
      xs.reduce(implicitly[Number[T]].plus(_, _)),
      xs.size
    )
}	
	
```

## Visitor Pattern

```scala
abstract class Element(text: String) {
  def accept(visitor: Visitor)
}

case class Title(text: String) extends Element(text) {
  override def accept(visitor: Visitor): Unit = {
    visitor.visit(this)
  }
}

case class Text(text: String) extends Element(text) {
  override def accept(visitor: Visitor): Unit = {
    visitor.visit(this)
  }
}

class Document(parts: List[Element]) {
  def accept(visitor: Visitor): Unit = {
    parts.foreach(p => p.accept(visitor))
  }
}

trait Visitor {
  def visit(element: Element)
}

class VisitorImpl1 extends Visitor { 
  override def visit(element: Element): Unit = {
    element match {
      case Title(text) => ???
      case Text(text) => ??? 
	  //...
	  }
  }
}
```

## Configuration

```scala
import com.typesafe.config.ConfigFactory

trait AppConfigComponent {

  val appConfigService: AppConfigService
  
  class AppConfigService() {
    //-Dconfig.resource=production.conf for overriding
    private val conf = ConfigFactory.load()
    private val appConf = conf.getConfig("job-scheduler")
    private val db = appConf.getConfig("db")
    
    val configPath = appConf.getString("config-path")
    val configExtension = appConf.getString("config-extension")
    val workers = appConf.getInt("workers")
    
    val dbConnectionString = db.getString("connection-string")
    val dbUsername = db.getString("username")
    val dbPassword = db.getString("password")
  }
}
```