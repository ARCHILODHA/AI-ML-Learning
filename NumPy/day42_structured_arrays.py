import numpy as np

# Define structured data type
student_dtype = [
    ("name", "U20"),
    ("age", "i4"),
    ("marks", "f4")
]

students = np.array([
    ("Arjun", 20, 85.5),
    ("Priya", 21, 92.0),
    ("Rahul", 19, 78.5),
    ("Neha", 20, 88.0)
], dtype=student_dtype)

print("Student Records:")
print(students)

# Access individual fields
print("\nStudent Names:")
print(students["name"])

print("\nStudent Ages:")
print(students["age"])

print("\nStudent Marks:")
print(students["marks"])

# Filter students
print("\nStudents Scoring Above 85:")
print(students[students["marks"] > 85])

# Sort by marks
sorted_students = np.sort(
    students,
    order="marks"
)

print("\nStudents Sorted by Marks:")
print(sorted_students)
