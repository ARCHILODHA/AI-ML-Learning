import pandas as pd

df = pd.DataFrame({"sales":[100,200,300,400]})

df["rolling_avg"] = df["sales"].rolling(2).mean()
print(df)
