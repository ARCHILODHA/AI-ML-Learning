# Day 34: Iterators in Python

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Custom Iterator

class CountUp:

    def __init__(self, maximum):
        self.current = 1
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.maximum:
            value = self.current
            self.current += 1
            return value
        raise StopIteration


counter = CountUp(5)

for number in counter:
    print("Count:", number)
