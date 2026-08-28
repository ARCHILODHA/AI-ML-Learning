# Day 26: Inheritance in Python

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


dog = Dog()
dog.eat()
dog.bark()

print()

cat = Cat()
cat.eat()
cat.meow()
