# a for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string )

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# loop through a string:
for x in "banana":
    print(x)

# the break statement:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# continue :
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# the range function:
for x in range(6):
    print(x)
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
    print(x)
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
print()
for x in range(2, 30, 3):
    print(x)


# else in for loop:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# the pass statement:
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
    pass
