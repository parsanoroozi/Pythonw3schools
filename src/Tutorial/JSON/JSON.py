# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.

# Python has a built-in package called json, which can be used to work with JSON data.
import json
# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
# some JSON:
# The result will be a Python dictionary.
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# you can convert other types to JSON:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Use the indent parameter to define the numbers of indents:

y = json.dumps(x, indent=2)
print(y)

# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

json.dumps(x, indent=4, separators=(". ", " = "))

# The json.dumps() method has parameters to order the keys in the result:
# sort_keys keyword
json.dumps(x, indent=4, sort_keys=True)