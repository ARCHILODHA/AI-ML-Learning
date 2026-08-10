import joblib

# Load Saved Model
model = joblib.load("model.pkl")

print("Model loaded successfully.")
print(model)
