# Day 33: enumerate() and zip()

names = ["Archi", "Rahul", "Priya"]
marks = [85, 90, 78]

print("Students:")

for index, name in enumerate(names, start=1):
    print(index, name)


print("\nStudent Marks:")

for name, mark in zip(names, marks):
    print(name, ":", mark)


subjects = ["Python", "Java", "DSA"]
scores = [90, 85, 95]

print("\nSubject Scores:")

for subject, score in zip(subjects, scores):
    print(f"{subject}: {score}")
