import pandas as pd

data = pd.Series([10, 20, 30, 40, 50])
bins = pd.cut(data, bins=3)

print(bins)
