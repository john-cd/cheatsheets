---
title: Python Links
category: python
tags: 
---

# Python useful links 


## Python environments

[venv — Creation of virtual environments]( https://docs.python.org/3/library/venv.html )

```bash
python3 -m venv /path/to/new/virtual/environment
```

[Virtualenv]( https://virtualenv.pypa.io/en/stable/  )

virtualenv is a tool to create isolated Python environments. Since Python 3.3, a subset of it has been integrated into the standard library under the venv module. Note though, that the venv module does not offer all features of this library (e.g. cannot create bootstrap scripts, cannot create virtual environments for other python versions than the host python, not relocatable, etc.). 

[pip-tools]( https://github.com/jazzband/pip-tools )

A set of command line tools to help you keep your pip-based packages fresh, even when you've pinned them.

[Pipenv]( https://pipenv.kennethreitz.org/en/latest/ )

The problems that Pipenv seeks to solve are multi-faceted:

- You no longer need to use pip and virtualenv separately. They work together.
- Managing a requirements.txt file can be problematic, so Pipenv uses Pipfile and Pipfile.lock to separate abstract dependency declarations from the last tested combination.
- Hashes are used everywhere, always. Security. Automatically expose security vulnerabilities.
- Strongly encourage the use of the latest versions of dependencies to minimize security risks arising from outdated components.
- Give you insight into your dependency graph (e.g. $ pipenv graph).
- Streamline development workflow by loading .env files.

[Pyenv]( https://realpython.com/intro-to-pyenv/ ) for managing multiple Python versions


## Testing

[Mockito]( https://mockito-python.readthedocs.io/en/latest/)

[Code coverage measurement for Python]( https://github.com/nedbat/coveragepy )

[mechanize - Automate interaction with HTTP web servers]( https://github.com/python-mechanize/mechanize )

## Packaging

[Cookiecutter template for a Python package]( https://github.com/audreyr/cookiecutter-pypackage )

[Python Packaging User Guide]( https://packaging.python.org/ )

[Twine]( https://github.com/pypa/twine )

Twine is a utility for publishing Python packages on PyPI.

## Build tools

[Buildout, an automation tool written in and extended with Python]( http://www.buildout.org/en/latest/ )

[PyBuilder]( https://pybuilder.github.io/ )

[Uranium: a Python Build System]( https://uranium.readthedocs.io/en/latest/ )

## Other

[Python Anywhere]( https://www.pythonanywhere.com/ )

Host, run, and code Python in the cloud
