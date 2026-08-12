import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Archi", "Rahul", "Priya", "Aman"],
    "Age": [20, np.nan, 19, 22],
    "Marks": [85, 78, np.nan, 88]
})

print("Original DataFrame:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

# Fill missing numeric values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter filling missing values:")
print(df)
