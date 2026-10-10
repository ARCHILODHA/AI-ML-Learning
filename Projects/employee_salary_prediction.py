import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = pd.DataFrame({
    "experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "projects": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "skills_score": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    "salary": [
        300000, 350000, 420000, 500000, 580000,
        650000, 720000, 800000, 900000, 1000000
    ]
})

X = data[["experience", "projects", "skills_score"]]
y = data["salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

error = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", round(error, 2))

new_employee = [[4, 5, 72]]

predicted_salary = model.predict(new_employee)

print(
    "Predicted Salary:",
    round(predicted_salary[0], 2)
)
