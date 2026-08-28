# Day 25: Classes and Objects

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student("Archi", 22, "AI/ML")
student2 = Student("Rahul", 21, "Python")

student1.display()
print()

student2.display()
