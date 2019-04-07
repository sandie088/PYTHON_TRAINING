# json in python
import json

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)


print(y["age"])


y = json.dumps(x)
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x, indent=4)
print(y)
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x, indent=4, separators=(". ", " = "))
print(y)
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True)
print(y)