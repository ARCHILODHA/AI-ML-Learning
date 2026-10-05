# Day 32: Shallow Copy and Deep Copy

import copy


original = [[1, 2], [3, 4]]

shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

original[0][0] = 100

print("Original:", original)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)


# Another example
numbers = [1, 2, 3, 4]

copied_numbers = numbers.copy()

copied_numbers.append(5)

print("Original List:", numbers)
print("Copied List:", copied_numbers)
