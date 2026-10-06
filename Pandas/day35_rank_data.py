import pandas as pd

df = pd.DataFrame({
    "Name": ["Archi", "Rahul", "Priya", "Aman", "Neha"],
    "Marks": [92, 85, 95, 78, 88]
})

df["Rank"] = df["Marks"].rank(
    ascending=False,
    method="dense"
).astype(int)

df = df.sort_values("Rank")

print("Student Ranking:")
print(df)
