# DeepSea 🌊

A Python library for Deep Learning & Machine Learning, focused on oceanographic and geospatial data.

## Installation
```bash
pip install git+https://github.com/YourGitHubUsername/DeepSea.git

## Usage

from DeepSea import LinearRegression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])
model = LinearRegression()
model.fit(X, y)
print(model.predict([[4]]))  # 8