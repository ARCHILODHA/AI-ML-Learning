import pandas as pd

df = pd.DataFrame({
    "Name": ["Archi", "Rahul", "Priya", "Aman"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 78, 92, 88]
})

print("DataFrame:")
print(df)

print("\nDataFrame information:")
df.info()

print("\nStatistical summary:")
print(df.describe())
