from tensorflow.keras.callbacks import ModelCheckpoint

checkpoint = ModelCheckpoint(
    "best_model.h5",
    save_best_only=True
)

print("Model checkpoint configured.")
