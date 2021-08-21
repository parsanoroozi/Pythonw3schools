# A tuple is a collection which is ordered and unchangeable.
mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(len(mytuple))
# tip
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# constructor => tuple()
# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# accessing the items is exactly like the lists

# a trick for being anle to change the tuple items:
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple. or we can append in this way. or...
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# for appending you can either use the list converting or add typle to a tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# for removing you can using lists or you can use del:
thistuple = ("apple", "banana", "cherry")
del thistuple

# unpacking tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# using asterisk => *:
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print()
print(green)
print(yellow)
print(red)

# loops in tuples are exactly like loops in lists...

# joining tuples are like lists besides you can multiply them:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
