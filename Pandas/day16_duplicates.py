import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "A", "C"]
})

print(df.drop_duplicates())
