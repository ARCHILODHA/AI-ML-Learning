import numpy as np

def detect_outliers(data):
    mean = np.mean(data)
    std = np.std(data)
    return [x for x in data if abs(x - mean) > 2 * std]
