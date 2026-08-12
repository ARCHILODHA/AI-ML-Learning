import pandas as pd

df = pd.DataFrame({
    "Name": ["Archi", "Rahul", "Priya", "Aman"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 78, 92, 88],
    "City": ["Delhi", "Mumbai", "Pune", "Jaipur"]
})

print("Original DataFrame:")
print(df)

# Drop City column
df = df.drop(columns=["City"])

print("\nAfter dropping City:")
print(df)

# Drop row with index 1
df = df.drop(index=1)

print("\nAfter dropping row:")
print(df)
