# A set is a collection which is both unordered and unindexed. and unorderd.
# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# constructor: => set()
thisset = set({"apple", "banana", "cherry"})  # note the double round-brackets
print(thisset)
print(type(thisset))

# accessing:
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)
# or

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# add : you cant change the items but you can add to them:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# or:
# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# to remove item in a set  use the remove() or the discard() method:
# remove():
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
# discard():
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
# Note: If the item to remove does not exist, discard() will NOT raise an error.
# and you can also use pop() to remove the last one
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# and also clear() and the del will empties the set:
thisset = {"apple", "banana", "cherry"}
del thisset
thisset = {"apple", "banana", "cherry"}
thisset.clear()

# you can loop through set with for:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


# for joining you cant use + but you can yse union() and update:
# union():
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# update():
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# you can keep only duplicates among two sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

# intersection() => this will return a new set:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# you can keep all except than duplicates:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#symmetric_differnce() => this will return a new set:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)