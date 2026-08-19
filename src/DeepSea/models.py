import numpy as np

class LinearRegression:
    def __init__(self):
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
        self.bias = theta[0]
        self.weights = theta[1:]
        
    def predict(self, X):
        X = np.array(X)
        return X.dot(self.weights) + self.bias