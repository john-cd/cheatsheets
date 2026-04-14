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
