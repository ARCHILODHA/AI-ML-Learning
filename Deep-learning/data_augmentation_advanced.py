import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import (
    RandomFlip,
    RandomRotation,
    RandomZoom
)

augmentation = Sequential([
    RandomFlip("horizontal"),
    RandomRotation(0.1),
    RandomZoom(0.1)
])

# Create a sample image
image = tf.random.uniform(
    shape=(1, 224, 224, 3)
)

augmented_image = augmentation(image)

print("Original shape:", image.shape)
print("Augmented shape:", augmented_image.shape)
print("Data augmentation completed.")
