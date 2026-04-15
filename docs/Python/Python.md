---
title: Python Links
category: python
tags:
---

# Python useful links

## Python environments

[uv](https://github.com/astral-sh/uv)

An extremely fast Python package installer and resolver, written in Rust. Designed as a drop-in replacement for `pip` and `pip-tools`.

[venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

```bash
python3 -m venv /path/to/new/virtual/environment
```

[Virtualenv](https://virtualenv.pypa.io/en/stable/)

virtualenv is a tool to create isolated Python environments. Since Python 3.3, a subset of it has been integrated into the standard library under the venv module. Note though, that the venv module does not offer all features of this library (e.g. cannot create bootstrap scripts, cannot create virtual environments for other python versions than the host python, not relocatable, etc.).

[pip-tools](https://github.com/jazzband/pip-tools)

A set of command line tools to help you keep your pip-based packages fresh, even when you've pinned them.

[Pipenv](https://pipenv.kennethreitz.org/en/latest/)

The problems that Pipenv seeks to solve are multi-faceted:

- You no longer need to use pip and virtualenv separately. They work together.
- Managing a requirements.txt file can be problematic, so Pipenv uses Pipfile and Pipfile.lock to separate abstract dependency declarations from the last tested combination.
- Hashes are used everywhere, always. Security. Automatically expose security vulnerabilities.
- Strongly encourage the use of the latest versions of dependencies to minimize security risks arising from outdated components.
- Give you insight into your dependency graph (e.g. $ pipenv graph).
- Streamline development workflow by loading .env files.

[Pyenv](https://realpython.com/intro-to-pyenv/) for managing multiple Python versions

## Testing

[Mockito]( https://mockito-python.readthedocs.io/en/latest/)

[Code coverage measurement for Python](https://github.com/nedbat/coveragepy)

[mechanize - Automate interaction with HTTP web servers](https://github.com/python-mechanize/mechanize)

## Packaging

[Cookiecutter template for a Python package](https://github.com/audreyr/cookiecutter-pypackage)

[Python Packaging User Guide](https://packaging.python.org/)

[Twine](https://github.com/pypa/twine)

Twine is a utility for publishing Python packages on PyPI.

## Build tools

[Buildout, an automation tool written in and extended with Python](https://www.buildout.org/en/latest/)

[PyBuilder](https://pybuilder.github.io/)

[Uranium: a Python Build System](https://uranium.readthedocs.io/en/latest/)

## Other

[Python Anywhere](https://www.pythonanywhere.com/)

Host, run, and code Python in the cloud

## Python 3

Python 3 is the current version of the Python programming language. It is a high-level, general-purpose programming language that emphasizes code readability with its notable use of significant indentation.

## What's new in Python 3.x

[What's really new in Python 3](https://powerfulpython.com/blog/whats-really-new-in-python-3/)

### nonlocal / global

```python
x = 0
def outer():
  x = 1
  def inner():
  nonlocal x
  x = 2
  print("inner:", x)

  inner()
  print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 2
# global: 0

## with global
x = 0
def outer():
     x = 1
     def inner():
           global x
           x = 2
           print("inner:", x)
  inner()
  print("outer:", x)
outer()
print("global:", x)

# inner: 2
# outer: 1
# global: 2
```

### String interpolation - new in 3.6

```python
name="David"
f"My name is {name}"
value = decimal.Decimal("10.4507")
print(f"result: {value:10.5}" )  # width precision
```

### PEP 492 - Coroutines with async and await syntax

[async and await](https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/)

``yield from iterator``

is equivalent

```python
for x in iterator:
     yield x
```

Example:

```python
def lazy_range(up_to):
     """Generator to return the sequence of integers from 0 to up_to, exclusive."""
     index = 0
     def gratuitous_refactor():
           nonlocal index
           while index < up_to:
               yield index
               index += 1
     yield from gratuitous_refactor()
```

New 3.12 syntax:

```python
async def func(param1, param2):
    do_stuff()
    await some_coroutine()

async def read_data(db):
  data = await db.fetch('SELECT ...')

async def display_date(loop):
  end_time = loop.time() + 5.0
  while True:
  print(datetime.datetime.now())
  if (loop.time() + 1.0) >= end_time:
  break
  await asyncio.sleep(1)


loop = asyncio.get_event_loop()# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(display_date(loop))
loop.close()
```

#### Async for

```python
async for TARGET in ITER:
  BLOCK
else:
  BLOCK2
```

#### Async improvements - 3.6

- set comprehension: ``{i async for i in agen()}``
- list comprehension: ``[i async for i in agen()]``
- dict comprehension: ``{i: i ** 2 async for i in agen()}``
- generator expression: ``(i ** 2 async for i in agen())``

### Type hinting

[PEP 484](https://www.python.org/dev/peps/pep-0484/)

[mypy-lang.org](https://mypy-lang.org/index.html)

```python
def greet(name: str) -> str
    return 'Hello there, {}'.format(name)
```

#### Type aliases

```python
Url = str
def retry(url: Url, retry_count: int) -> None: ...
```

```python
from typing import TypeVar, Iterable, Tuple
```

Other common typings include: Any; Generic, Dict, List, Optional, Mapping, Set, Sequence - expressed as Sequence[int]

```python
T = TypeVar('T', int, float, complex)  # T is either or an int, a float or a complex
Vector = Iterable[Tuple[T, T]]          #

def inproduct(v: Vector[T]) -> T:
       return sum(x*y for x, y in v)

def dilate(v: Vector[T], scale: T) -> Vector[T]:
       return ((x * scale, y * scale) for x, y in v)
vec = [] # type: Vector[float]
```

#### For functions

```python
Callable[[Arg1Type, Arg2Type], ReturnType]
```

#### Type comments

```python
x = []   # type: List[Employee]
x, y, z = [], [], []  # type: List[int], List[int], List[str]
```

## Modern Python Features

### Type Hinting (Python 3.5+)

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

### f-strings (Python 3.6+)

```python
name = "World"
print(f"Hello {name}")
```

### Data Classes (Python 3.7+)

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0
```

### Walrus Operator (Python 3.8+)

```python
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```

### Match Statement (Python 3.10+)

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

## Dataclasses

Dataclasses (introduced in Python 3.7) provide a decorator and functions for automatically adding generated special methods such as `__init__()` and `__repr__()` to user-defined classes.

```python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```

## Asyncio

Asyncio is a library to write concurrent code using the `async`/`await` syntax.

```python
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())
```

## Type Hinting

Type hinting allows you to explicitly state the expected type of arguments and return values.

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```
