---
title: Scikit-Learn
category: datascience
tags: data
---

## Useful Links

[Cheatsheet- Scikit-Learn & Caret Package for Python & R respectively](https://www.analyticsvidhya.com/blog/2016/12/cheatsheet-scikit-learn-caret-package-for-python-r-respectively/?utm_content=buffer3140b&utm_medium=social&utm_source=linkedin.com&utm_campaign=buffer)
## Modern API Features

- **Pipeline**: `make_pipeline` for easier composition.
- **ColumnTransformer**: For applying transformations to different column types.
- **HistGradientBoostingClassifier**: Fast gradient boosting.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier

# Pipeline
clf = make_pipeline(StandardScaler(), HistGradientBoostingClassifier())

# Column Transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['numerical_col']),
        ('cat', OneHotEncoder(), ['categorical_col'])
    ])
```
