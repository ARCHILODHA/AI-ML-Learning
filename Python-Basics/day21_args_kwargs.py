# Day 21 - *args and **kwargs

# *args allows multiple positional arguments

def calculate_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print("Sum:", calculate_sum(10, 20))
print("Sum:", calculate_sum(10, 20, 30))
print("Sum:", calculate_sum(1, 2, 3, 4, 5))


# **kwargs allows multiple keyword arguments

def display_student(**details):
    print("\nStudent Details:")

    for key, value in details.items():
        print(key, ":", value)


display_student(
    name="Archi",
    branch="CSE",
    age=20,
    city="Udaipur"
)


# Combining normal arguments, *args and **kwargs

def student_info(name, *skills, **details):

    print("\nName:", name)

    print("Skills:")
    for skill in skills:
        print("-", skill)

    print("Other Details:")
    for key, value in details.items():
        print(key, ":", value)


student_info(
    "Archi",
    "Python",
    "Java",
    "DSA",
    github="ARCHILODHA",
    branch="CSE"
)
