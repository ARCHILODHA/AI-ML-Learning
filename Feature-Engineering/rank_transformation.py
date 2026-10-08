import pandas as pd

data = pd.DataFrame({
    "Name": ["Archi", "Rahul", "Priya", "Aman", "Neha"],
    "Score": [95, 82, 90, 75, 88]
})

data["Rank"] = data["Score"].rank(
    ascending=False,
    method="dense"
).astype(int)

print("Original Data:")
print(data[["Name", "Score"]])

print("\nRank Transformed Data:")
print(data)
