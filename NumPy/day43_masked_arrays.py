import numpy as np

# Create an array containing invalid values
data = np.array([10, 20, -999, 40, 50, -999, 70])

# Mask invalid values
masked_data = np.ma.masked_equal(data, -999)

print("Original Array:")
print(data)

print("\nMasked Array:")
print(masked_data)

print("\nMask:")
print(masked_data.mask)

print("\nMean Without Invalid Values:")
print(masked_data.mean())

print("\nMaximum Valid Value:")
print(masked_data.max())

print("\nMinimum Valid Value:")
print(masked_data.min())

# Fill masked values
filled_data = masked_data.filled(0)

print("\nArray After Filling Masked Values:")
print(filled_data)
