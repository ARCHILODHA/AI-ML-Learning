import pandas as pd

df = pd.DataFrame({
    "Name": ["Archi", "Rahul", "Priya", "Aman", "Neha"],
    "Marks": [90, 75, 88, 95, 82],
    "City": ["Udaipur", "Jaipur", "Delhi", "Udaipur", "Jaipur"]
})

print("Original DataFrame:")
print(df)

high_marks = df.query("Marks >= 85")

print("\nStudents with Marks >= 85:")
print(high_marks)

udaipur_students = df.query("City == 'Udaipur'")

print("\nStudents from Udaipur:")
print(udaipur_students)

combined = df.query("Marks >= 85 and City == 'Udaipur'")

print("\nUdaipur Students with Marks >= 85:")
print(combined)
