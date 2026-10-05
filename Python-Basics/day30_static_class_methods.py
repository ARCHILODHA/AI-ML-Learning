# Day 30: Static Method and Class Method

class Student:

    college = "Techno NJR"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

    @staticmethod
    def is_pass(marks):
        return marks >= 40


student = Student("Archi", 85)

student.display()

print("College:", Student.college)
print("Passed:", Student.is_pass(student.marks))

Student.change_college("Techno NJR Institute of Technology")

print("Updated College:", Student.college)
