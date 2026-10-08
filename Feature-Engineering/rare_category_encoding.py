import pandas as pd

data = pd.DataFrame({
    "City": [
        "Udaipur",
        "Jaipur",
        "Delhi",
        "Udaipur",
        "Mumbai",
        "Kota",
        "Ajmer",
        "Udaipur"
    ]
})

frequency = data["City"].value_counts()

threshold = 2

data["City_Grouped"] = data["City"].apply(
    lambda city: city
    if frequency[city] >= threshold
    else "Other"
)

print("Original Data:")
print(data[["City"]])

print("\nRare Category Encoded Data:")
print(data)
