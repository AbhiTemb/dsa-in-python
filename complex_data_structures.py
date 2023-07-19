'''
ARRAY METHODS:

1. slice: pick a slice of a collection i.e. list, tuple, string
sliced = collection[start: stop: step]
step: takes a step size on start
negative step: goes in opposite direction ie end to start
'''
L = [0, 45, 45, 234, 7450]

# Slice
print(L)
print(L[0:4:2])
print(L[1:])
print(L[:2])
print(L[::2])
print(L[::-2])

# Reverse a string using slice
name = "Rabbit"
reverse_name = name[::-1]
print(reverse_name)

'''
SETS:
set is an unordered unique collection of elements =>
no duplicates, no frequency tracking, no order of elements

set is extremely fast for lookup of elements
no order of elements exist hence addition/removal of elements is fast
'''

# set is declared using set literals
s = { 1, 3453, 34, 1 ,2340 }
# however, to declare empty set we cannot use set literals because {} creates an empty dictionary instead
S = set() # empty set
print(type({}))

print(s)

# set addition
S.add(0)
print(S)

# set removal
# S.remove(5) # this will give keyError because 5 is not present in set
S.remove(0) 
print(S)

# check presence of a key: O(1) time
S.add(0)
S.add(3435235234)
print(0 in S)
print(39045 in S)

# in operator can also be used in list: O(n) time
print(35435 in L)
print(7450 in L)

print(s.union(S))
print(s.difference(S)) 
print(s.intersection(S))

'''
DICTIONARY:
d = { 'key': 4}
It's a collection of key value pairs
uses a hash function just like set hence fast lookup
lookup time
O(1) time
'''
d = {'key':8}
print(d['key'])

# to create a new key use
d['spaces'] = 12

# to check key in dictionary
print('key' in d) # to check key wise

# to print out all keys or values
print(d.keys())
print(d.values())
# better to convert these to list
print(list(d.keys()))
print(list(d.values()))

# delete key in dictionary
del d['key']
print(d)

# Iterating over dictionary
d['rabbit'] = 34
d['duck'] = 34535

for key, value in d.items():
    print(key, value)

for key in d:
    print(key, d[key])

'''
LIST COMPREHENSIONS:
x = [x for x in range(5)]
x is a list that is generated from for loop
'''

x = [x for x in range(5)]
print("LIST COMPREHENSION", x)

# list comprehension that doubles each element in range 0 to 4
x = [2 * x for x in range(5)]

x = [[0 for j in range(4)] for i in range(4)]
print(x)

# Complex list comprehensions
# with If conditions
x = [ i for i in range(100) if i%5 == 0]
print(x)

# for dictionaries
x = { i:"value" for i in range(100) if i%5 == 0}
print(x)

# for sets
x = {i for i in range(100) if i%5 == 0}
print(x)

# for tuples
x = tuple( i for i in range(100) if i%5 == 0)
print(x)

