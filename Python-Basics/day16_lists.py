# Day 16 - Lists in Python

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# Add elements
numbers.append(60)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

# Remove elements
numbers.remove(30)
print("After remove:", numbers)

removed = numbers.pop()
print("Removed element:", removed)
print("List after pop:", numbers)

# Sorting
numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)

# Slicing
print("First three:", numbers[:3])

# Finding length
print("Number of elements:", len(numbers))

# Iterating through list
print("List elements:")

for number in numbers:
    print(number)
