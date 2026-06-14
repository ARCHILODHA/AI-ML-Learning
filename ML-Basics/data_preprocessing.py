from sklearn.preprocessing import LabelEncoder

data = ["Cat", "Dog", "Cat", "Bird"]

encoder = LabelEncoder()
encoded = encoder.fit_transform(data)

print(encoded)
