import numpy as np
from sklearn.metrics import mean_squared_error

y_true = np.array([
    10,
    20,
    30,
    40,
    50
])

y_pred = np.array([
    12,
    18,
    29,
    43,
    48
])

mse = mean_squared_error(y_true, y_pred)

rmse = np.sqrt(mse)

print("Mean Squared Error:", mse)

print("Root Mean Squared Error:", rmse)
