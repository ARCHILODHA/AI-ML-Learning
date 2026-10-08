import numpy as np
from sklearn.preprocessing import QuantileTransformer

data = np.array([
    [10],
    [20],
    [25],
    [30],
    [100],
    [500]
])

transformer = QuantileTransformer(
    output_distribution="normal",
    random_state=42
)

transformed = transformer.fit_transform(data)

print("Original Data:")
print(data.flatten())

print("\nQuantile Transformed Data:")
print(np.round(transformed.flatten(), 3))
