# regex example
import re
import camelcase

txt = "The rain in chennai"
x = re.search("^The.*chennai$", txt)
print(x.string)

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)

str = "The rain in Spain"
x = re.split("\s", str)
print(x)

c = camelcase.CamelCase()
print(c.hump(str))

try:
    f = open("test.txt")
    print(f)
except:
    print("No such file found")
finally:
    print("Finished with try catch block")