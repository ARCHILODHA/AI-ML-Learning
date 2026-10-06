import pandas as pd

df = pd.DataFrame({
    "Maths": [80, 90, 75, 88, 95],
    "Python": [85, 92, 78, 90, 96],
    "DSA": [70, 88, 80, 85, 94]
})

print("Marks DataFrame:")
print(df)

print("\nTotal Marks:")
print(df.sum(axis=1))

print("\nAverage Marks:")
print(df.mean(axis=1))

print("\nMaximum Marks:")
print(df.max(axis=1))

print("\nMinimum Marks:")
print(df.min(axis=1))

df["Total"] = df.sum(axis=1)
df["Average"] = df.mean(axis=1)

print("\nUpdated DataFrame:")
print(df)
