from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(X.toarray())
