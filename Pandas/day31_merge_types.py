import pandas as pd

students = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Archi", "Rahul", "Priya", "Aman"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [90, 85, 88]
})

inner = pd.merge(students, marks, on="ID", how="inner")
left = pd.merge(students, marks, on="ID", how="left")
right = pd.merge(students, marks, on="ID", how="right")
outer = pd.merge(students, marks, on="ID", how="outer")

print("Inner Join:")
print(inner)

print("\nLeft Join:")
print(left)

print("\nRight Join:")
print(right)

print("\nOuter Join:")
print(outer)
