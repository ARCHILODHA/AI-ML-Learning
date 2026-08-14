# Day 17 - Tuples in Python

student = ("Archi", 20, "CSE", 8.7)

print("Student tuple:", student)

# Accessing elements
print("Name:", student[0])
print("Age:", student[1])
print("Branch:", student[2])
print("CGPA:", student[3])

# Tuple length
print("Length:", len(student))

# Tuple slicing
print("First two values:", student[:2])

# Tuple unpacking
name, age, branch, cgpa = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)
print("CGPA:", cgpa)

# Nested tuple
courses = (
    ("Python", 90),
    ("Java", 85),
    ("DBMS", 88)
)

for course, marks in courses:
    print(course, ":", marks)

# Tuple methods
numbers = (10, 20, 10, 30, 10)

print("Count of 10:", numbers.count(10))
print("Position of 30:", numbers.index(30))
