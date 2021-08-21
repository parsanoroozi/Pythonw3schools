# Exception handling

# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.
x = 2
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# using else:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# finally
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


# Raise an exception:
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")


# You can define what kind of error to raise, and the text to print to the user.
# Raise a TypeError if x is not an integer:
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
