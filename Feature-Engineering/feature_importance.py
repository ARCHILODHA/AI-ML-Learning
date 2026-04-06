from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X, y)

print(model.feature_importances_)
