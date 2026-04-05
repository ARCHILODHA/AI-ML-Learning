import pandas as pd

df = pd.DataFrame({'marks':[50,70,90]})

print(df[df['marks'] > 60])
