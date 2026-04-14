---
title: Scikit-Learn
category: datascience
tags: data
---

## Useful Links

[Scikit-Learn Documentation](https://scikit-learn.org/stable/)

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
