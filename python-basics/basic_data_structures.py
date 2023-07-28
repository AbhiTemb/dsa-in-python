'''
COLLECTIONS:
An ordered or unordered group of elements

1. List: [1,2,3,4,5]
2. Tuple: ('a', 'b', 'c', 'd')

Contents of collections need not be of same datatype
'''

'''
List : Ordered collection, order of elements are maintained
'''
L = ['a',2,0,4.8]
print(L, len(L))

# Len can also be used for strings
print(len('abcddfewagfa'))

# Append to the end of the list, can add a list as a element of the list here
L.append('lmao')
print(L)

append_list = [1,2,3,4]
append_list.append(['a','b','c','d'])
print(append_list)

# Extend list by adding more elements
L.extend(['this','is','rabbit','group'])
print(L)

# List methods
# pop element from end of the list
print(L.pop())

# List is mutable hence we can change any element at a position in a list
# L stores reference to the list data structure
L[0] = 1
print(L.pop(1),L)

# L stores reference to the list , so L1 now also points to L's list
L1 = L
print(L1, L)

'''
Tuple : Immutable data structure, similar to List but cannot append, change, remove an element to tuple 
    They are like a immutable list
'''

T = (0,1,2,3,4)
# T[0] = 1 #wrong , T is immutable

A = [[], (), [[[[]]]]] # nesting of tuples & list is allowed
# nested lists no need to be of uniform size

