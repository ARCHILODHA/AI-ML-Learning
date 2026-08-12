import pandas as pd

df = pd.DataFrame({
    "Name": ["Archi", "Rahul", "Priya", "Aman"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 78, 92, 88]
})

print("Using loc:")
print(df.loc[0:2, ["Name", "Marks"]])

print("\nUsing iloc:")
print(df.iloc[0:3, 0:2])
