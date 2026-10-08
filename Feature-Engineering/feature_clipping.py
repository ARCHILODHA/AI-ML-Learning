import pandas as pd

data = pd.DataFrame({
    "Salary": [
        25000,
        30000,
        35000,
        40000,
        45000,
        500000
    ]
})

lower_limit = data["Salary"].quantile(0.05)
upper_limit = data["Salary"].quantile(0.95)

data["Salary_Clipped"] = data["Salary"].clip(
    lower=lower_limit,
    upper=upper_limit
)

print("Original Data:")
print(data[["Salary"]])

print("\nClipped Data:")
print(data)

print("\nLower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
