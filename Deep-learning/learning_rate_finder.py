import tensorflow as tf

# Load MNIST
(x_train, y_train), _ = tf.keras.datasets.mnist.load_data()

x_train = x_train.astype("float32") / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

# Start with a small learning rate
optimizer = tf.keras.optimizers.Adam(
    learning_rate=0.001
)

model.compile(
    optimizer=optimizer,
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    x_train,
    y_train,
    epochs=3,
    batch_size=64
)

print("Training completed with learning rate:", 0.001)
