import pandas as pd

df = pd.read_csv("../Datasets/student_data.csv")

print(df.isnull().sum())
df = df.dropna()

print(df.head())
