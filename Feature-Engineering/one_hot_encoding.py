import pandas as pd

# Sample data
df = pd.DataFrame({
    "City": ["Delhi", "Mumbai", "Delhi", "Pune"]
})

# One Hot Encoding
encoded = pd.get_dummies(df, columns=["City"])

print(encoded)
