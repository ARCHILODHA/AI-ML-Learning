import pandas as pd

df = pd.DataFrame({
    "date": ["2024-01-01", "2024-02-01"]
})

df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year

print(df)
