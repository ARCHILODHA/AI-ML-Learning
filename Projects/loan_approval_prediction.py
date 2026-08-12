import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.DataFrame({
    "Income": [25000, 50000, 30000, 80000, 45000, 90000, 35000, 70000],
    "CreditScore": [600, 750, 620, 800, 680, 820, 640, 780],
    "LoanAmount": [200000, 300000, 250000, 400000, 280000, 500000, 220000, 350000],
    "Education": ["Graduate", "Graduate", "Not Graduate", "Graduate",
                  "Graduate", "Graduate", "Not Graduate", "Graduate"],
    "Approved": ["No", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes"]
})

encoder = LabelEncoder()
data["Education"] = encoder.fit_transform(data["Education"])
data["Approved"] = encoder.fit_transform(data["Approved"])

X = data.drop("Approved", axis=1)
y = data["Approved"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

sample = [[60000, 740, 300000, 0]]
print("Loan approval prediction:", model.predict(sample))
