# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

# The values in dictionary items can be of any data type:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

# reaching Items:
# simple:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
# with get():
x = thisdict.get("model")

# get keys => keys():
x = thisdict.keys()
print(x)

# get values => values():
y = thisdict.values()
print(y)

# get items():
a = thisdict.items()
print(a)

# check if key exist:
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# changing items:
# simply change:
thisdict["year"] = 2018
# update() method:
thisdict.update({"year": 2020})

# adding an item:
# simply add:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# using updat() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})


# removing items:
# with pop():
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)
# with popitem():
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

# with del:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# 1:
del thisdict["model"]
# 2:
del thisdict

# with clear():
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# loop through the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)
# or:
for x in thisdict:
    print(thisdict[x])
# or:
for x in thisdict.values():
    print(x)
# or:
for x in thisdict.keys():
    print(x)
# or even you can get both of keys and values:
for x, y in thisdict.items():
    print(x, y)

# copying is exactly as the same as list...


# Nested dictionary
# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
# or if you want to add three dicts into a new one:
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
