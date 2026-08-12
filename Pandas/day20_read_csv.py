import pandas as pd

# Create a sample CSV file
data = {
    "Name": ["Archi", "Rahul", "Priya"],
    "Age": [20, 21, 19],
    "Marks": [85, 78, 92]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

# Read CSV
loaded_df = pd.read_csv("students.csv")

print("Data loaded from CSV:")
print(loaded_df)
