import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Create sequence data
X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7],
    [6, 7, 8]
], dtype=np.float32)

y = np.array([4, 5, 6, 7, 8, 9], dtype=np.float32)

# Reshape for RNN
X = X.reshape((X.shape[0], X.shape[1], 1))

model = Sequential([
    SimpleRNN(32, activation="tanh", input_shape=(3, 1)),
    Dense(1)
])

model.compile(
    optimizer="adam",
    loss="mse"
)

model.fit(X, y, epochs=100, verbose=0)

sample = np.array([7, 8, 9], dtype=np.float32)
sample = sample.reshape((1, 3, 1))

prediction = model.predict(sample, verbose=0)

print("Predicted next value:", prediction[0][0])
