import tensorflow as tf

adam = tf.keras.optimizers.Adam(learning_rate=0.001)
sgd = tf.keras.optimizers.SGD(learning_rate=0.01)
rmsprop = tf.keras.optimizers.RMSprop(learning_rate=0.001)

print("Optimizers initialized.")
