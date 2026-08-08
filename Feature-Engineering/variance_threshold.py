from sklearn.feature_selection import VarianceThreshold
import pandas as pd

df = pd.DataFrame({
    "A":[1,1,1,1],
    "B":[1,2,3,4],
    "C":[2,2,2,2]
})

selector = VarianceThreshold(threshold=0)

new_data = selector.fit_transform(df)

print(new_data)
