---
title: C# Cheatsheet
category: dotNET
tags: .NET C#
comments: true 
---

# C# Cheatsheets

[Quick Reference](http://www.digilife.be/quickreferences/qrc/core%20csharp%20and%20.net%20quick%20reference.pdf)

[Cheatsheet](https://www.cheatography.com/kimyo/cheat-sheets/c/)


# C# 6.0 / 7.0 - what is new

### Readonly properties

```csharp
public string FirstName { get; private set; }  // private set is accessible from the entire class

public string LastName { get; } // accessible only in constructor

public ICollection<double> Grades { get; } = new List<double>(); // property initializer
```

### Expression-bodied function members

```csharp
public override string ToString() => "Hi!";
```

### Using static

```csharp
using static System.String;
// also common: 
// using static System.Math;
// using static System.Linq.Enumerable;

if (IsNullOrWhiteSpace(lastName))
  throw new ArgumentException(message: "Cannot be blank", paramName: nameof(lastName));
```

### Null checking

```csharp
var first = person?.FirstName;
first = person?.FirstName ?? "Unspecified";

// preferred event handing in C# 6:
this.SomethingHappened?.Invoke(this, eventArgs);
```

### String interpolation

```csharp
public string GetFormattedGradePoint() => $"Name: {LastName}, {FirstName}. G.P.A: {Grades.Average():F2}";
```

### Exception Filters

```csharp
public static async Task<string> MakeRequest()
{
  var client = new System.Net.Http.HttpClient();
  var streamTask = client.GetStringAsync("https://localHost:10000");
  try 
  {
    var responseText = await streamTask;
    return responseText;
  } 
  catch (System.Net.Http.HttpRequestException e) when (e.Message.Contains("301"))
  {
  return "Site Moved";
  }
}
```

### List and dict initializers

```csharp
private List<string> messages = new List<string>
{
  "Page not Found",
  "Page moved, but left a forwarding address.",
  "The web server can't come out to play today."
};

private Dictionary<int, string> webErrors = new Dictionary<int, string>
{
  [404] = "Page not Found",
  [302] = "Page moved, but left a forwarding address.",
  [500] = "The web server can't come out to play today."
};
```

### Out variables

```csharp
if (int.TryParse(input, out int result))
    WriteLine(result);
else
    WriteLine("Could not parse input");
```
    
### Tuples

```csharp
var letters = ("a", "b");

(string Alpha, string Beta) namedLetters = ("a", "b");
var alphabetStart = (Alpha: "a", Beta: "b");

public class Point
{
  public Point(double x, double y)
  {
  this.X = x;
  this.Y = y;
  }

  public double X { get; }
  public double Y { get; }

  // Deconstruct method
  public void Deconstruct(out double x, out double y)
  {
  x = this.X;
  y = this.Y;
  }
}
```

### Ref return values

```csharp
public static ref int Find3(int[,] matrix, Func<int, bool> predicate)
{
  for (int i = 0; i < matrix.GetLength(0); i++)
             for (int j = 0; j < matrix.GetLength(1); j++)
                      if (predicate(matrix[i, j]))
                          return ref matrix[i, j];
  throw new InvalidOperationException("Not found");
}
ref var item = ref MatrixSearch.Find3(matrix, (val) => val == 42);
Console.WriteLine(item);
item = 24;
Console.WriteLine(matrix[4, 2]);
```

### Local functions

```csharp
public static IEnumerable<char> AlphabetSubset3(char start, char end)
{
    if ((start < 'a') || (start > 'z'))
        throw new ArgumentOutOfRangeException(paramName: nameof(start), message: "start must be a letter");
    if ((end < 'a') || (end > 'z'))
        throw new ArgumentOutOfRangeException(paramName: nameof(end), message: "end must be a letter");
    if (end <= start)
        throw new ArgumentException($"{nameof(end)} must be greater than {nameof(start)}");
    return alphabetSubsetImplementation();

    IEnumerable<char> alphabetSubsetImplementation()
    {
        for (var c = start; c < end; c++)
            yield return c;
    }
}
```