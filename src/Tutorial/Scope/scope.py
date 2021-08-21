# you can asign a global variable inside of an scope or function with the global keyword:
def myfunc():
    global x
    x = 300


myfunc()

print(x)

# Also, use the global keyword if you want to make a change to a global variable inside a function.

x = 300


def myfunc():
    global x
    x = 200


myfunc()

print(x)
