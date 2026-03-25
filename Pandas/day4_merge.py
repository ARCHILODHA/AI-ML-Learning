import pandas as pd

df1 = pd.DataFrame({"id":[1,2], "name":["A","B"]})
df2 = pd.DataFrame({"id":[1,2], "marks":[90,80]})

print(pd.merge(df1, df2, on="id"))
