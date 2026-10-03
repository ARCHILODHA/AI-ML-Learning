import numpy as np
from sklearn.metrics import mean_absolute_error

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

mae = mean_absolute_error(y_true, y_pred)

print("Mean Absolute Error:", mae)
