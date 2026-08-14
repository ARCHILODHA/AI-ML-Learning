# Day 23 - Working with JSON

import json

student = {
    "name": "Archi",
    "age": 20,
    "branch": "CSE",
    "skills": ["Python", "Java", "DSA"]
}

# Convert Python dictionary into JSON string

json_data = json.dumps(student, indent=4)

print("JSON Data:")
print(json_data)


# Convert JSON string back into Python object

python_data = json.loads(json_data)

print("\nPython Dictionary:")
print(python_data)

print("\nStudent Name:", python_data["name"])


# Write JSON to a file

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("\nstudent.json file created successfully.")


# Read JSON from file

with open("student.json", "r") as file:
    data = json.load(file)

print("\nData read from file:")
print(data)
