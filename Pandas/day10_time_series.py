import pandas as pd

dates = pd.date_range('2025-01-01', periods=5)
df = pd.DataFrame({'date': dates})

print(df)
