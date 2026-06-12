from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense

model = Sequential([
    GRU(64, input_shape=(100, 1)),
    Dense(1)
])

print("Basic GRU model created.")
