import pandas as pd

df = pd.DataFrame({
    'city': ['A','B','A','C'],
    'target': [1,0,1,0]
})

mean = df.groupby('city')['target'].mean()
df['encoded'] = df['city'].map(mean)

print(df)
