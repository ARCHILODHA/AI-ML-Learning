import pandas as pd

df = pd.DataFrame({
    "ID": range(1, 11),
    "Name": [
        "Archi", "Rahul", "Priya", "Aman", "Neha",
        "Riya", "Karan", "Ankit", "Sneha", "Vikas"
    ],
    "Marks": [90, 85, 88, 76, 95, 82, 79, 91, 87, 84]
})

print("Complete DataFrame:")
print(df)

sample_rows = df.sample(n=3, random_state=42)

print("\nRandom Sample:")
print(sample_rows)

sample_fraction = df.sample(frac=0.3, random_state=42)

print("\n30% Random Sample:")
print(sample_fraction)
