from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

messages = [
    "Win a free lottery prize",
    "Congratulations you won money",
    "Claim your free reward now",
    "Meeting scheduled for tomorrow",
    "Please send the project report",
    "Your assignment submission is due"
]

labels = [
    "spam",
    "spam",
    "spam",
    "ham",
    "ham",
    "ham"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(messages)

model = LogisticRegression()
model.fit(X, labels)

new_messages = [
    "Congratulations you won a free prize",
    "Please send me the report"
]

new_X = vectorizer.transform(new_messages)

predictions = model.predict(new_X)

for message, prediction in zip(new_messages, predictions):
    print(message)
    print("Prediction:", prediction)
    print()
