import numpy as np

# Sample datasets
study_hours = np.array([1, 2, 3, 4, 5])
marks = np.array([40, 50, 60, 70, 85])

# Calculate correlation
correlation = np.corrcoef(study_hours, marks)

# Calculate covariance
covariance = np.cov(study_hours, marks)

print("Study Hours:")
print(study_hours)

print("\nMarks:")
print(marks)

print("\nCorrelation Matrix:")
print(correlation)

print("\nCovariance Matrix:")
print(covariance)

print("\nCorrelation Coefficient:")
print(correlation[0, 1])
