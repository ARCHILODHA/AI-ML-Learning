import numpy as np

def dropout(x, drop_prob=0.5):
    mask = np.random.rand(*x.shape) > drop_prob
    return x * mask
