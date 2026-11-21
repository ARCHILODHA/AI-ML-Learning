import numpy as np

# Generate sample data
np.random.seed(42)

data = np.random.normal(
    loc=50,
    scale=10,
    size=1000
)

# Calculate histogram
frequencies, bin_edges = np.histogram(
    data,
    bins=10
)

print("Histogram Frequencies:")
print(frequencies)

print("\nBin Edges:")
print(bin_edges)

print("\nTotal Observations:")
print(np.sum(frequencies))

print("\nMean:")
print(np.mean(data))

print("\nStandard Deviation:")
print(np.std(data))
