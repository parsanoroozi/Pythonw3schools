# List is a collection which is ordered and changeable. Allows duplicate members.
mylist = ['apple', 'banna', 'cherry']
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(mylist)
print(len(mylist))

# a list can contain different data types
list1 = ["abc", 34, True, 40, "male"]
print(list1)

print(type(list1))

# list constructor list()
thisList = list(('apple', 'banna', 'cherry'))
print(thisList)
thisList = list(['apple', 'banna', 'cherry'])
print(thisList)

# access list items:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thisList[2:5])

# check if item exists:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

    # change items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# if you insert more itmes than you replace, the nowe items will be inserted where you specified
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist[1:3] = ["watermelon"]
print(thislist)

# insert items:
thislist.insert(2, "watermelon")
print(thislist)

# append items:
# to add an Item to the end of the list:
thislist.append("orange")
print(thislist)

# extend:
# to append a list into end of the list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# remove Item => remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# remove specified index => pop() or del[]
# actually del also can remove the whole list
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# clear list makes the list empty
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# loop through the list:
# similar to foreach:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# similar to for:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# loop through the list with while:
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# comprehension
# this is for creating a shorter syntax for some stuff
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist = [expression for item in iterable if condition == True]
newlist = [x+'Eddited' for x in fruits if "a" in x]
print(newlist)
# instead of:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# sort lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

# customize sort function:


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# case insensetive sort:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# reverse()
# just reversing the order regardless of the alphabet:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# copy list:
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# join list:
#There are several ways to join, or concatenate, two or more lists in Python.
#1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#2:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#3:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)