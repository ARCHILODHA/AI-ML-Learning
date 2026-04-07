import pandas as pd

df = pd.DataFrame({'marks':[50,90,70]})
print(df.sort_values('marks'))
