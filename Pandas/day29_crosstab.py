import pandas as pd

df = pd.DataFrame({
    "Gender": ["Female", "Male", "Female", "Male", "Female"],
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi"],
    "Result": ["Pass", "Pass", "Pass", "Fail", "Pass"]
})

print("Original DataFrame:")
print(df)

print("\nCity vs Gender:")
print(pd.crosstab(df["City"], df["Gender"]))

print("\nCity vs Result:")
print(pd.crosstab(df["City"], df["Result"]))
