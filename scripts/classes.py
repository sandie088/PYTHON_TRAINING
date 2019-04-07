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
    def __init__(self, name, age, skill):
        TestClass.__init__(self, name, age)
        self.skill = skill

    def printSkill(self):
        print(self.skill)

    def toString(self):
        print("Child details --> Name: {}, Age: {} and Skill:{}".format(self.name, self.age, self.skill))

child = ChildClass("Child", 2, "Run")
child.printName()
child.printSkill()
child.toString()