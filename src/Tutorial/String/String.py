a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello world!"
print(a[0])
print(a[len(a) - 1])

# looping through the string
for x in a:
    print(x)

# check in:
txt = 'The best things in life are free!'
if "free" in txt:
    print('yes its in there!')
else:
    print('no its no there')

# check not:
if 'expensive' not in txt:
    print('yes you are right. Its not there')

# slice:

b = 'hello_world!'
print(b)
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:])
print(b[-5:-1])
print(b[-5:-2])

# modify strings :

# upper case and lower case:
a = 'Hello World!'
print(a.upper())
print(a.lower())

# remove whitespace
a = ' Hello, world! '
print(a)
print(a.strip())

# replace:
a = 'Hello, World!'
print(a.replace('o', '+'))

# split:
arr = a.split(',')
for x in arr:
    print(x)
    
# concatination:
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#format:
#ths format is totally wrong:
# age = 36
# txt = "My name is John, I am " + age

#but there is a solution:
age = 36
txt = 'My name is John, and I am {}'
x = txt.format(age)
print(x)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#or you can use index numbers to be sure about the orders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#for using illegal characters as a real char in string you should put \ next to them
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

