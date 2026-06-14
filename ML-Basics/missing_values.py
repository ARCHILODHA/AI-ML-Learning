import pandas as pd

data = {
    "Age": [20, None, 25],
    "Marks": [80, 90, None]
}

df = pd.DataFrame(data)

print(df.fillna(df.mean(numeric_only=True)))
