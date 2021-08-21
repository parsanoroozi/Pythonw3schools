# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
a = 33
b = 200
if b > a:
    print("b is greater than a")
# elif:
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# else:
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# short hand if:
# if you have only one statement to execute, you can put it on the same line as the if statement:
if a > b:
    print("a is greater than b")

# or:
a = 2
b = 330
print("A") if a > b else print("B")

# one line if else with 3 conditoins:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# and :
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# or :
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# the pass statement:
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
    pass
