# Day 20 - Dictionary Comprehension

# Create dictionary using normal loop

squares = {}

for number in range(1, 6):
    squares[number] = number * number

print("Using normal loop:", squares)

# Dictionary comprehension

square_dict = {
    number: number * number
    for number in range(1, 6)
}

print("Using comprehension:", square_dict)

# Even number dictionary

even_numbers = {
    number: number * number
    for number in range(1, 11)
    if number % 2 == 0
}

print("Even number squares:", even_numbers)

# Student marks

marks = {
    "Python": 85,
    "Java": 78,
    "DBMS": 90,
    "OS": 72
}

# Subjects with marks >= 80

high_scores = {
    subject: score
    for subject, score in marks.items()
    if score >= 80
}

print("High scores:", high_scores)

# Convert list into dictionary

names = ["Archi", "Rahul", "Priya"]

name_lengths = {
    name: len(name)
    for name in names
}

print("Name lengths:", name_lengths)
