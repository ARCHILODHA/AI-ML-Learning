import pandas as pd

df = pd.DataFrame({
    "Name": ["Archi", "Rahul", "Priya", "Aman"],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune"],
    "Marks": [85, 78, 92, 88]
})

print("Original DataFrame:")
print(df)

# Replace Delhi with Jaipur
df["City"] = df["City"].replace("Delhi", "Jaipur")

print("\nAfter replacement:")
print(df)
