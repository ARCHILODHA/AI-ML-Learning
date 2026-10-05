# Day 31: Local and Global Scope

x = 100


def display_global():
    print("Global x:", x)


def local_example():
    x = 50
    print("Local x:", x)


def modify_global():
    global x
    x = 200


display_global()
local_example()

print("Before modification:", x)

modify_global()

print("After modification:", x)
