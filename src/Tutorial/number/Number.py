import random

x = 1  # int
y = 2.8  # float
z = 2 + 1j  # complex

print(type(x))
print(type(y))
print(type(z))

# random:

a = random.randrange(1, 25)
print(a)


def calculateRand():
    print(random.randrange(1, 10))
