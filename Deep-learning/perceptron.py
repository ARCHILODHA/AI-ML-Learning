import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=10):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0

    def activation(self, value):
        return 1 if value >= 0 else 0

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)

        self.weights = np.zeros(X.shape[1])

        for _ in range(self.epochs):
            for features, target in zip(X, y):
                linear_output = np.dot(features, self.weights) + self.bias

                prediction = self.activation(linear_output)

                error = target - prediction

                self.weights += self.learning_rate * error * features
                self.bias += self.learning_rate * error

    def predict(self, X):
        X = np.array(X)

        predictions = []

        for features in X:
            value = np.dot(features, self.weights) + self.bias
            predictions.append(self.activation(value))

        return np.array(predictions)


X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

y = [0, 0, 0, 1]

model = Perceptron()

model.fit(X, y)

predictions = model.predict(X)

print("Predictions:", predictions)
