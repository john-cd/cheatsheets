---
title: ASP.NET Core app
category: dotNET
tags: .NET C# ASP.NET
comments: true
---

## Using Yeoman to generate a ASP.NET Core app from a template

### Install Node.js and npm

To get started with Yeoman, install [Node.js](https://nodejs.org/en/). The installer includes Node.js and [npm](https://www.npmjs.com/).

- for Mac OS X
```bash
brew install node
``` 

- for Windows OS
```bash
choco install nodejs
```


### Install [Yeoman](http://yeoman.io/) and [Bower](https://bower.io/)


```bash
npm install -g yo

npm install -g bower
```

### Install [generator-aspnet](https://www.npmjs.com/package/generator-aspnet)
        
```bash
npm install -g generator-aspnet
```

Run with 
```bash
yo aspnet
```

See also: [Building Projects with Yeoman on docs.asp.net](https://docs.microsoft.com/en-us/aspnet/core/client-side/yeoman)


### Optionaly install the [yeoman extension](https://marketplace.visualstudio.com/items?itemName=samverschueren.yo) in Visual Studio Code


## Architecture

[Onion Architecture In ASP.NET Core MVC](http://www.c-sharpcorner.com/article/onion-architecture-in-asp-net-core-mvc/)

[Example of a Web API built on ASP.NET Core](https://github.com/juunas11/AspNetCoreApiExample/tree/basic-api)



## [Routing Examples](https://joonasw.net/view/attribute-routing-cheat-sheet-for-aspnet-core)

```csharp
public class TestController : Controller
{

// /hello
[Route("/hello")]
public IActionResult Hello() => Ok("Hello");

// /hi only GET method
[Route("/hi")] [HttpGet]
public IActionResult Hi() => Ok("Hi");

//Alternative for previous
[HttpGet("/hi")]
public IActionResult Hi() => Ok("Hi");
}

//Route prefix
[Route("test")]
public class TestController2 : Controller
{
//You can have multiple routes on an action
[Route("")] // /test
[Route("hello")]  // /test/hello
public IActionResult Hello() => Ok("Hello");

// Maps to both: // /test/hi, and: // /hi
[Route("/hi")] // Overrides the prefix with /, you can also use ~/
[Route("hi")]
public IActionResult Hi() => Ok("Hi");

// /test/greet/Joon -> maps Joon to the name parameter
[Route("greet/{name}")]
public IActionResult Greet(string name) => Ok($"Hello {name}!");

//Parameters can be optional
// /test/greetopt -> name == null
// /test/greetopt/Joon -> name == Joon
[Route("greetopt/{name?}")]
public IActionResult GreetOptional(string name) => Ok(name == null ? "No name" : "Hi!");
}

// You can use [controller], [action], and [area] to create generic templates
[Route("[controller]/[action]")]
public class MyController : Controller
{
// /my/info
public IActionResult Info() => Ok("Info");
// /my/i
[Route("/[controller]/i")]
public IActionResult Info2() => Ok("Info2"); }

[Route("users")]
public class SelectionController : Controller
{
//You can use constraints to influence route selection
//Do not use for validation!
// /users/123
[Route("{id:int}")]
public IActionResult Int(int id) => Ok($"Looked up user id {id}");
 
// /users/joonas
[Route("{name:alpha}")]
public IActionResult String(string name) => Ok($"User name {name}"); 
}
```
