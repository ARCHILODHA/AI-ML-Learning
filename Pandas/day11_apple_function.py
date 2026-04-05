import pandas as pd

df = pd.DataFrame({'a':[1,2,3]})

df['b'] = df['a'].apply(lambda x: x*2)
print(df)
