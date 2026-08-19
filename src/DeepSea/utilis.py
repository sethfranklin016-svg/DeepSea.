import numpy as np

def normalize_depth(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data) + 1e-8)

def load_ocean_data(file_path, x_column, y_column):
    import pandas as pd
    df = pd.read_csv(file_path)
    X = df[x_column].values.reshape(-1, 1)
    y = df[y_column].values
    return X, y