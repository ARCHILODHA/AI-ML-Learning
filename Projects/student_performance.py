import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "PreviousMarks": [50, 55, 60, 65, 70, 75, 80, 85],
    "FinalMarks": [52, 57, 63, 68, 73, 78, 84, 90]
})

X = data[["StudyHours", "Attendance", "PreviousMarks"]]
y = data["FinalMarks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

student = [[7, 90, 82]]

print("Predicted final marks:", model.predict(student))
