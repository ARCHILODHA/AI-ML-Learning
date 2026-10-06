import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Archi", "Rahul"],
    "Marks": [90, 85]
})

df2 = pd.DataFrame({
    "Name": ["Priya", "Aman"],
    "Marks": [88, 92]
})

result = pd.concat([df1, df2], ignore_index=True)

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

print("\nAfter Concatenation:")
print(result)
