import pandas as pd
import numpy as np

data = pd.DataFrame({
    "Age": [20, 22, 24, 25, 26, 30, 35, 40, 45, 50],
    "Salary": [
        25000,
        28000,
        30000,
        32000,
        35000,
        40000,
        50000,
        65000,
        80000,
        150000
    ]
})

for column in data.columns:
    print(f"\n--- {column} ---")

    print("Mean:", data[column].mean())
    print("Median:", data[column].median())
    print("Standard Deviation:", data[column].std())
    print("Minimum:", data[column].min())
    print("Maximum:", data[column].max())

    skewness = data[column].skew()

    print("Skewness:", round(skewness, 3))

    if skewness > 0:
        print("Distribution: Positively Skewed")
    elif skewness < 0:
        print("Distribution: Negatively Skewed")
    else:
        print("Distribution: Approximately Symmetric")
