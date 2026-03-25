from sklearn.preprocessing import LabelEncoder

data = ["cat", "dog", "cat"]

le = LabelEncoder()
print(le.fit_transform(data))
