import pandas as pd

df = pd.DataFrame({
    "x":[1,2,3,4],
    "y":[2,4,6,8]
})

print(df.corr())
