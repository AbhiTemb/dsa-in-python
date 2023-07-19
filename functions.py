'''
FUNCTIONS:
functions are objects in python and hence can be passed in arguments or returned from another function
'''

def sample_function():
    print("Function runs")

sample_function()

def outer_function():
    print("Here we are !")
    def inner_function():
        print("We are inside another function")
    inner_function()

outer_function()

# Passing parameters
def multiply_and_divide(x, y):
    print("RUN", x, y)
    return x * y, x / y

# returns a tuple here
print(multiply_and_divide(4,2))

# unpack the returned values
r1, r2 = multiply_and_divide(4,2)
print(r1, r2)

# inconvenenient way
print(multiply_and_divide(4,2)[0], multiply_and_divide(4,2)[1])

# Optional parameters
def func(x, y, z=None):
    print("Parameters", x, y, z)

# here x and y are required parameters, but z is optional parameter
func(4,0)
func(1,2,3)

'''
Advanced concepts of functions:
'''

# treating functions as objects
def outer(x):
    def inner():
        print(x)

    return inner

# outer.locals.inner => inner function is defined within outer function
print(outer(23535)) # returns inner function
print("OUTER", outer(34535)()) 

# Unpack operator: *
x = [1, 2, 3, 4, 5]
'''
Separates all the elements of x into individual elements, picks out all elements and
 passes them one by one into print statement

Behaves same like spread operator of js
'''
print("Unpack operator", *x) 

def print_function(x, y):
    print(x, y)

pairs = [(1,2),(3,4)]
for pair in pairs:
    print_function(*pair)

# for dictionaries
print_function(**{'y': 800, 'x': 900})

'''
To spread
To spread the arguments into a function use these
For dictionaries: **
For list, tuples: * 

To accept
**kwargs(keyword arguments) to accept unlimited number of keyword arguments for a function
packs arguments into dictionary
*args(arguments) to accept unlimited number of arguments for a function
packs arguments into list
'''

def func(*args, **kwargs):
    print(args, kwargs)

func(1,2,3,4,5,one=1,two=2)

'''
GLOBAL scope:
by default variables are local scope
to access global variables we have to global variables
'''

'''
Exception Handling
'''

#raise Exception('Error')
# raise FileExistsError()

# handle exception
try:
    x = 5/0
except Exception as e: #same as catch statement
    print(e)
finally:
    print("Next statement")

'''
Lambda function:
One liner function that is anonymous there
'''
x = lambda x: x+2
print(x(5))

# Map function
L = [1,2,3,4,5]
mp = map(lambda i:i+2, x)

# Filter function
fl = map(lambda i:i%2==0, x)
print(list(mp))

print(f'hello { 40+49 } with { 12 + 34}')
