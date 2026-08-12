import pandas as pd

df = pd.DataFrame({
    "City": [
        "Delhi",
        "Mumbai",
        "Delhi",
        "Pune",
        "Mumbai",
        "Jaipur"
    ]
})

print("Unique cities:")
print(df["City"].unique())

print("\nNumber of unique cities:")
print(df["City"].nunique())

print("\nFrequency of each city:")
print(df["City"].value_counts())
