import pandas as pd

data = pd.DataFrame({
    "City": [
        "Udaipur",
        "Jaipur",
        "Udaipur",
        "Delhi",
        "Jaipur",
        "Udaipur"
    ]
})

frequency = data["City"].value_counts(normalize=True)

data["City_Frequency"] = data["City"].map(frequency)

print("Original Data:")
print(data[["City"]])

print("\nFrequency Encoded Data:")
print(data)
