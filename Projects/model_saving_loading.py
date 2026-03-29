import joblib

# save
joblib.dump(model, "model.pkl")

# load
model = joblib.load("model.pkl")
