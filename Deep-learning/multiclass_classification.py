import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Load Iris dataset
iris = tf.keras.utils.get_file(
    "iris.csv",
    "https://raw.githubusercontent.com/"
    "plotly/datasets/master/iris-data.csv"
)

print("Dataset downloaded successfully.")

# Simple multi-class neural network
model = Sequential([
    Dense(32, activation="relu", input_shape=(4,)),
    Dense(16, activation="relu"),
    Dense(3, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()
