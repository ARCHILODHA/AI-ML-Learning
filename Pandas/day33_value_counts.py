import pandas as pd

df = pd.DataFrame({
    "City": ["Udaipur", "Jaipur", "Udaipur", "Delhi", "Jaipur", "Udaipur"],
    "Result": ["Pass", "Pass", "Fail", "Pass", "Fail", "Pass"]
})

print("DataFrame:")
print(df)

print("\nCity Frequency:")
print(df["City"].value_counts())

print("\nResult Frequency:")
print(df["Result"].value_counts())

print("\nResult Percentage:")
print(df["Result"].value_counts(normalize=True) * 100)

print("\nUnique Cities:")
print(df["City"].nunique())
