import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense

# Example vocabulary
vocab_size = 1000
embedding_dimension = 16

model = Sequential([
    Embedding(
        input_dim=vocab_size,
        output_dim=embedding_dimension
    ),

    GlobalAveragePooling1D(),

    Dense(32, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()

print("Embedding model created successfully.")
