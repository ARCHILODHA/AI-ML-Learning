import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Sample Input
sample = np.array([[5.1, 3.5, 1.4, 0.2]])

prediction = model.predict(sample)

print("Prediction:", prediction)
