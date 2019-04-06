# Function demo

def printThis(text = "Printing this"):
        print(text)
        return True

if(printThis()):
    print("success")
printThis("Hello All")

# lambda expressions
x = lambda a, b : a ** b
print(x(7349787983479834799, 6))

# Arrays example
array = ["This", "That", "Those", "And", "Those"]
print(array)

array.pop(0)
print(array)

array.remove("And")
print(array)