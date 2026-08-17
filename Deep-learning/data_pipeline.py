import tensorflow as tf

# Create sample dataset
features = tf.constant([
    [1.0, 2.0],
    [2.0, 3.0],
    [3.0, 4.0],
    [4.0, 5.0],
    [5.0, 6.0]
])

labels = tf.constant([0, 0, 1, 1, 1])

dataset = tf.data.Dataset.from_tensor_slices(
    (features, labels)
)

# Shuffle, batch and prefetch
dataset = dataset.shuffle(5)
dataset = dataset.batch(2)
dataset = dataset.prefetch(tf.data.AUTOTUNE)

for batch_features, batch_labels in dataset:
    print("Features:")
    print(batch_features)

    print("Labels:")
    print(batch_labels)
    print("---")
