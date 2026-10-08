import pandas as pd
from sklearn.preprocessing import PowerTransformer

data = pd.DataFrame({
    "Income": [1000, 1500, 2000, 5000, 10000, 50000]
})

transformer = PowerTransformer(method="yeo-johnson")

transformed = transformer.fit_transform(data)

result = pd.DataFrame(
    transformed,
    columns=["Income_Transformed"]
)

print("Original Data:")
print(data)

print("\nPower Transformed Data:")
print(result)
