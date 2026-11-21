import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Calculate percentiles
p25 = np.percentile(data, 25)
p50 = np.percentile(data, 50)
p75 = np.percentile(data, 75)

# Calculate quantiles
quantiles = np.quantile(data, [0.25, 0.50, 0.75])

print("Dataset:")
print(data)

print("\n25th Percentile:", p25)
print("50th Percentile:", p50)
print("75th Percentile:", p75)

print("\nQuantiles:")
print(quantiles)

# Interquartile range
iqr = p75 - p25

print("\nInterquartile Range:", iqr)
