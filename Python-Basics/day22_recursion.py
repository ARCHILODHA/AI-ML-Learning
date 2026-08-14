# Day 22 - Recursion in Python

# Factorial using recursion

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))


# Sum of numbers using recursion

def sum_numbers(n):

    if n == 0:
        return 0

    return n + sum_numbers(n - 1)


print("Sum from 1 to 10:", sum_numbers(10))


# Fibonacci using recursion

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci sequence:")

for i in range(10):
    print(fibonacci(i), end=" ")

print()


# Countdown using recursion

def countdown(n):

    if n == 0:
        print("Done!")
        return

    print(n)
    countdown(n - 1)


print("\nCountdown:")
countdown(5)
