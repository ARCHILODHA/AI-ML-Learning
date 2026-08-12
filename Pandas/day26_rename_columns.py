import pandas as pd

df = pd.DataFrame({
    "student_name": ["Archi", "Rahul", "Priya"],
    "student_age": [20, 21, 19],
    "student_marks": [85, 78, 92]
})

print("Original columns:")
print(df)

df = df.rename(columns={
    "student_name": "Name",
    "student_age": "Age",
    "student_marks": "Marks"
})

print("\nRenamed columns:")
print(df)
