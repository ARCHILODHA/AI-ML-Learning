from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential([
    LSTM(64, input_shape=(100, 1)),
    Dense(1)
])

print("Basic LSTM model created.")
