# Day 18 - Sets in Python

numbers = {10, 20, 30, 40, 50}

print("Original set:", numbers)

# Add element
numbers.add(60)
print("After add:", numbers)

# Remove element
numbers.remove(20)
print("After remove:", numbers)

# Duplicate values are automatically removed
values = {10, 20, 20, 30, 30, 40}

print("Set with duplicates removed:", values)

# Set operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference A-B:", a.difference(b))
print("Difference B-A:", b.difference(a))

# Membership
print("3 in a:", 3 in a)
print("10 in a:", 10 in a)

# Loop through set
for value in a:
    print("Value:", value)
