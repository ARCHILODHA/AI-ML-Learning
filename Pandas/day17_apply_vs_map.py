import pandas as pd

df = pd.DataFrame({"marks":[10,20,30]})

df["double"] = df["marks"].apply(lambda x: x*2)
print(df)
