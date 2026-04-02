import pandas as pd

df = pd.read_csv("data.csv")

print(pd.pivot_table(df, values='salary', index='department'))
