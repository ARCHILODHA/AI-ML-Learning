import pandas as pd

df = pd.DataFrame({
    "Name": ["archi lodha", "rahul sharma", "PRIYA SINGH"],
    "City": ["udaipur", "jaipur", "delhi"]
})

print("Original DataFrame:")
print(df)

df["Name_Upper"] = df["Name"].str.upper()
df["Name_Lower"] = df["Name"].str.lower()
df["City_Title"] = df["City"].str.title()

print("\nAfter String Operations:")
print(df)

print("\nNames containing 'rahul':")
print(df[df["Name"].str.contains("rahul", case=False)])

print("\nName Length:")
print(df["Name"].str.len())
