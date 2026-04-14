---
title: Matplotlib Cheatsheet
category: python
tags: data visualization
---

# Matplotlib Cheatsheet

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

- Main page: <https://matplotlib.org>
- Image gallery: <https://matplotlib.org/stable/gallery/index.html>
- Examples <https://matplotlib.org/stable/plot_types/index.html>
- Tutorial: <https://matplotlib.org/stable/tutorials/index.html>

## Basic Plotting (Modern Object-Oriented API)

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a Figure and an Axes
fig, ax = plt.subplots()

# Plot data on the Axes
ax.plot(x, y, label='sin(x)')

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Simple Plot')
ax.legend()

# Show plot
plt.show()
```
