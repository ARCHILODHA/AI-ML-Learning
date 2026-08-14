# Day 19 - Dictionaries in Python

student = {
    "name": "Archi",
    "age": 20,
    "branch": "CSE",
    "cgpa": 8.7
}

print("Student:", student)

# Access values
print("Name:", student["name"])
print("Branch:", student["branch"])

# get()
print("CGPA:", student.get("cgpa"))

# Add new key
student["city"] = "Udaipur"
print("After adding city:", student)

# Update value
student["cgpa"] = 9.0
print("Updated CGPA:", student)

# Remove key
student.pop("age")
print("After removing age:", student)

# Dictionary keys
print("Keys:", student.keys())

# Dictionary values
print("Values:", student.values())

# Dictionary items
print("Items:")

for key, value in student.items():
    print(key, ":", value)

# Check key
if "name" in student:
    print("Name exists in dictionary")
