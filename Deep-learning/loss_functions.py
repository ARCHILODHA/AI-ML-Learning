iimport numpy as np

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def binary_crossentropy(y_true, y_pred):
    return -np.mean(y_true*np.log(y_pred) + (1-y_true)*np.log(1-y_pred))
