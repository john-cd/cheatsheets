---
title: Python 3
category: python
tags: 
---

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

New 3.6 syntax:

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

[mypy-lang.org](http://mypy-lang.org/index.html)

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