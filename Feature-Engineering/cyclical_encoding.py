import pandas as pd
import numpy as np

data = pd.DataFrame({
    "Month": [1, 2, 3, 6, 12],
    "DayOfWeek": [0, 1, 2, 5, 6]
})

data["Month_Sin"] = np.sin(
    2 * np.pi * data["Month"] / 12
)

data["Month_Cos"] = np.cos(
    2 * np.pi * data["Month"] / 12
)

data["Day_Sin"] = np.sin(
    2 * np.pi * data["DayOfWeek"] / 7
)

data["Day_Cos"] = np.cos(
    2 * np.pi * data["DayOfWeek"] / 7
)

print("Cyclical Encoded Features:")
print(data)
