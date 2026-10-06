import pandas as pd

df = pd.DataFrame({
    "Name": ["Archi", "Rahul", "Priya", "Aman"],
    "Marks": [90, 85, 88, 92],
    "City": ["Udaipur", "Jaipur", "Delhi", "Udaipur"]
})

print("DataFrame:")
print(df)

print("\nMemory Usage:")
print(df.memory_usage(deep=True))

print("\nTotal Memory Usage:")
print(df.memory_usage(deep=True).sum(), "bytes")

print("\nData Types:")
print(df.dtypes)

df["City"] = df["City"].astype("category")

print("\nMemory Usage After Category Conversion:")
print(df.memory_usage(deep=True))

print("\nUpdated Data Types:")
print(df.dtypes)
