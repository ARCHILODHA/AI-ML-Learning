import pandas as pd

def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

df = pd.read_csv("sample.csv")
df = clean_data(df)
print(df.head())
