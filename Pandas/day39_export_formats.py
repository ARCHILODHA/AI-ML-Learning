import pandas as pd

df = pd.DataFrame({
    "Name": ["Archi", "Rahul", "Priya"],
    "Marks": [90, 85, 88],
    "City": ["Udaipur", "Jaipur", "Delhi"]
})

print("Original DataFrame:")
print(df)

# Export to CSV
df.to_csv("students.csv", index=False)

# Export to JSON
df.to_json("students.json", orient="records", indent=4)

print("\nFiles exported successfully.")

# Read JSON file
loaded_json = pd.read_json("students.json")

print("\nData Read From JSON:")
print(loaded_json)

# Convert DataFrame to dictionary
data_dict = df.to_dict(orient="records")

print("\nData as Dictionary:")
print(data_dict)
