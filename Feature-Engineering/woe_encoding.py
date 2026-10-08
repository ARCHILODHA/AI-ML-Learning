import pandas as pd
import numpy as np

data = pd.DataFrame({
    "City": [
        "Udaipur",
        "Udaipur",
        "Jaipur",
        "Jaipur",
        "Delhi",
        "Delhi"
    ],
    "Target": [1, 1, 0, 1, 0, 0]
})

total_good = (data["Target"] == 0).sum()
total_bad = (data["Target"] == 1).sum()

stats = data.groupby("City")["Target"].agg(
    ["count", "sum"]
)

stats["bad"] = stats["sum"]
stats["good"] = stats["count"] - stats["bad"]

stats["good_distribution"] = (
    stats["good"] / total_good
)

stats["bad_distribution"] = (
    stats["bad"] / total_bad
)

stats["WOE"] = np.log(
    stats["good_distribution"] /
    stats["bad_distribution"]
)

print("WOE Statistics:")
print(stats)

data["City_WOE"] = data["City"].map(stats["WOE"])

print("\nWOE Encoded Data:")
print(data)
