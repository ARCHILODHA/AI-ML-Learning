import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

data = pd.DataFrame({
    "action_score": [9, 8, 7, 2, 1, 3, 2, 8, 9, 1],
    "comedy_score": [2, 3, 2, 9, 8, 7, 9, 3, 2, 8],
    "drama_score": [4, 3, 5, 7, 6, 8, 7, 4, 3, 7],
    "genre": [
        "Action",
        "Action",
        "Action",
        "Comedy",
        "Comedy",
        "Drama",
        "Comedy",
        "Action",
        "Action",
        "Drama"
    ]
})

X = data[["action_score", "comedy_score", "drama_score"]]
y = data["genre"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

new_movie = [[8, 2, 4]]

prediction = model.predict(new_movie)

print("\nPredicted Genre:", prediction[0])
