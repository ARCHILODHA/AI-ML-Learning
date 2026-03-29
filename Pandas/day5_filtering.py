import pandas as pd

df = pd.read_csv("sample.csv")

print(df[df['marks'] > 80])
