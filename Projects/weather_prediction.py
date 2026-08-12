import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.DataFrame({
    "Temperature": [15, 18, 22, 25, 30, 32, 35, 20],
    "Humidity": [80, 75, 65, 60, 50, 45, 40, 70],
    "Rain": [1, 1, 0, 0, 0, 0, 0, 1]
})

X = data[["Temperature", "Humidity"]]
y = data["Rain"]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

weather = [[21, 68]]

prediction = model.predict(weather)

if prediction[0] == 1:
    print("Rain is likely.")
else:
    print("Rain is unlikely.")
