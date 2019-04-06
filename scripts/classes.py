# classes example

class TestClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print(self.name)

emp = TestClass("Admin", 20)

print(emp, " ", emp.name, " ", emp.age)
emp.printName()

class ChildClass(TestClass):
    pass

child = ChildClass("Child", 2)
child.printName()