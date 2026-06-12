from tensorflow.keras.applications import MobileNetV2

model = MobileNetV2(weights='imagenet', include_top=False)

print("Transfer Learning model loaded.")
