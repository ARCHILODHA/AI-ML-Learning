nums = [1,2,3,4,5]

# Lambda
square = lambda x: x*x

# Map
print(list(map(square, nums)))

# Filter
print(list(filter(lambda x: x%2==0, nums)))
