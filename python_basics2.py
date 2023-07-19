'''
ARITHMETIC OPERATORS
'''
x = 12
y = 2535
result = x + y
print(result)

x = 19
y = 234.0
result = x + y # Automatically converts result to float
print(result)

x = 12
y = 4
result = x / y # Automatically converts result to float because python always performs division in floating point because it doesn't know whether to return result in some level of precision or not
print(result)

# To avoid precision, use //
x = 94
y = 2
result = x // y
result2 = x / y
print(result, result2)

x = 12
y = 11
result = x / y 
print(result)

# EXPONENTIATION
x = 2
y = 54
print(x ** y)

# MODULO
x = 345435
y = 2
print(x % y)

'''
STRING METHODS:
'''
upper_case = 'hello'.upper()
print(upper_case)

lower_case = "HULLO".lower()
print(lower_case)

captialize_string = "hElLo WorlD".capitalize()
print(captialize_string)

count_substring = "hello WorLd".count("l")
print(count_substring)

# Method chaining is also allowed
print("thiS Is A STRING".lower().capitalize())

# String multiplication
x = "Hello"
y = 5
print(x * y)

# String addition: concatenation
x = "Kratos"
y = "World"
print(x + y)

'''
CONDITIONALS:
evaluates to a boolean value

Conditional operators : ==, !=, >=, <=, <, >
'''

print("hello" == 'hello') # True

# We can compare strings also !
print('a' > 'Z') # True
print('ASCII value of a: ', ord('a'))
print('ASCII value of Z: ', ord('Z'))

'''
compare strings by comparing corresponding characters from left to right
if false encountered, we declare result
ex:
cde > aza
c > a || d > z || e > a
True || False || .... = True
'''
print('ab' < 'ac')
print('cde' > 'aza')

# Arithmetic operators: and, or, not
print('a' < 'z' or 'w' > 'l')

# Order of arithmetic operators : not > and > or


'''
CONTROL STRUCTURES:
if else, elif
'''

name = input('Enter your name: ')

if name == 'Abhinav':
    print('You are an instructor')
elif name == 'Adonis':
    print('You are great bro!')
else:
    print("You are a student")

print("This is outside block")
