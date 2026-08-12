import pandas as pd

data = {
    "Name": ["Archi", "Rahul", "Priya"],
    "Marks": [85, 78, 92]
}

df = pd.DataFrame(data)

# Save to Excel
df.to_excel("students.xlsx", index=False)

# Read Excel
loaded_df = pd.read_excel("students.xlsx")

print("Data loaded from Excel:")
print(loaded_df)
