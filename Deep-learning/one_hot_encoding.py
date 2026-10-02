import numpy as np

def one_hot_encode(labels, num_classes):
    encoded = np.zeros((len(labels), num_classes), dtype=int)

    for i, label in enumerate(labels):
        encoded[i, label] = 1

    return encoded


labels = [0, 2, 1, 3, 2]

encoded = one_hot_encode(labels, 4)

print("Original labels:")
print(labels)

print("\nOne-hot encoded labels:")
print(encoded)
