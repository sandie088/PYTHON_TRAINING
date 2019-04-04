# list example
nameList = ["alpha", "beta", "gamma"]
print(nameList)
nameList[1] = "Baetaaa"
print(nameList)
if "alpha" in nameList:
    print("alpha is in ", nameList)

del nameList[0]
print(nameList)

nameList.append("alpha")
print(nameList)

nameList.append("alpha")
print(nameList)

anotherList = nameList
print(anotherList)

anotherList.reverse()
print(anotherList)

for x in anotherList:
    print(x)

# tuples are list of constants
testTuple = ("success", "failure", "in progress")
print(testTuple)
print(testTuple.count("success"))

for x in testTuple:
    print(x)

# examples of set
testSet = {"apple", "orange", "banana"}
print(testSet)
testSet.add("apple")
print(testSet)

for x in testSet:
    print(x)

testSet.update(["grapes", "guava"])
print(testSet)
# print("-- Enter fruit to be added --")
# testSet.add(input())
print(testSet)

# dictionaries are list json or hash map

testDictionary = {
    "id": 123214,
    "name" : "test name",
    "status" : True
}

print(testDictionary)

print(testDictionary.get("status"))

testDictionary["status"]  = False
print(testDictionary.get("status"))

for x in testDictionary:
    print(x," : ", testDictionary[x])

for x, y in testDictionary.items():
    print(x, " : ", y)

cardict = dict(brand="Ford", model="Mustang", year=1964)
print(cardict)