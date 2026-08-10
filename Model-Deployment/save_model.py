from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Train Model
model = RandomForestClassifier()
model.fit(X, y)

# Save Model
joblib.dump(model, "model.pkl")

print("Model saved successfully.")
