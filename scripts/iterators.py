import variables
# Example of iterators in python
testTuple = ("Alpha", "Beta", "Gamma")
iterator = iter(testTuple)

for x in iterator:
    print(x)

class IntNumbers:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a <= 100:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


intNum = IntNumbers()
iterator = iter(intNum)

for x in iterator:
    print(x)

print(variables.nameList)