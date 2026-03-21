import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Marks": [90, 80, 85]
}

df = pd.DataFrame(data)

print(df)
print("Average:", df["Marks"].mean())
