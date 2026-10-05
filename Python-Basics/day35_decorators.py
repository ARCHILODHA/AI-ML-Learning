# Day 35: Decorators in Python

def logger(function):

    def wrapper():
        print("Function execution started")
        function()
        print("Function execution completed")

    return wrapper


@logger
def greet():
    print("Hello, Archi!")


greet()


# Decorator with arguments

def uppercase(function):

    def wrapper(name):
        result = function(name)
        return result.upper()

    return wrapper


@uppercase
def welcome(name):
    return f"Welcome {name}"


print(welcome("Archi"))
