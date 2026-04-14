---
title: Flask
category: python
tags: web
---

# Flask

Flask is a lightweight WSGI web application framework.

## Modern Flask (3.x) Best Practices

- Use `flask run` instead of `app.run()`
- Use Application Factories

```python
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

### Useful Flask modules

[Flask-Login](https://pypi.org/project/Flask-Login/)

[Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)

