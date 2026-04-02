import pandas as pd

df['new_col'] = df['marks'].apply(lambda x: x * 2)
