import pandas as pd

data = {
    "Name": ["A", "B", "A"],
    "Marks": [90, 80, 70]
}

df = pd.DataFrame(data)

print(df.groupby("Name").mean())
