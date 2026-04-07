import pandas as pd

df = pd.DataFrame({'a':[1,None,3]})
df.fillna(0, inplace=True)

print(df)
