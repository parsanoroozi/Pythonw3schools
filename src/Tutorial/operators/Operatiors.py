x, y = 25, 3

# arithmetic operators
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# assignment Operators
x = 13
x += 3
x -= 3
x *= 3
x /= 3
x %= 3
x //= 3
x **= 3


# comparision operators
#  	Equal	x == y
# 	Not equal	x != y
# 	Greater than	x > y
# 	Less than	x < y
# 	Greater than or equal to	x >= y
#   Less than or equal to	x <= y

# logical operators:
x = 1
if not x == 2:
    print('x is not 1')

if x == 1 and x != 3:
    print('x is one and its not 3')
  
if x ==1 or x ==2:
  print('x is either one or two')
  
#Identity operators:
if x is y:
  print('x is y')
if x is not y:
  print('x is not y')
  
#membership operators:
x = 'table, desk, pen, earaser, pencil'
y = 'ta'
if y in x:
  print('x is in y')
if y not in x:
  print('x is not in y')
  
#bitwise operators:
# x &= 3
# x |= 3
# x ^= 3
# x ~= 3
# x >>= 3
# x <<= 3