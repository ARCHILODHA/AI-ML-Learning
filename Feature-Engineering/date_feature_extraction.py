import pandas as pd

df = pd.DataFrame({
    "Date": pd.to_datetime([
        "2025-01-15",
        "2025-05-20",
        "2025-10-10"
    ])
})

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

print(df)
