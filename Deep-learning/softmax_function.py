import numpy as np

def softmax(values):
    values = np.array(values)

    values = values - np.max(values)

    probabilities = np.exp(values) / np.sum(np.exp(values))

    return probabilities


scores = [2.0, 1.0, 0.1]

result = softmax(scores)

print("Softmax probabilities:")

for i, probability in enumerate(result):
    print(f"Class {i}: {probability:.4f}")

print("Probability sum:", np.sum(result))
