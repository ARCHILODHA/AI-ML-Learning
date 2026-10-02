import tensorflow as tf

class SquareLayer(tf.keras.layers.Layer):
    def call(self, inputs):
        return tf.square(inputs)


model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(3,)),
    SquareLayer(),
    tf.keras.layers.Dense(4, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()

sample_input = tf.constant([
    [1.0, 2.0, 3.0]
])

output = model(sample_input)

print("\nModel output:")
print(output.numpy())
