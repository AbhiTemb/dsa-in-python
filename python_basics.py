'''
DATATYPES:
Four data types in python : 
Int, Float, String, Bool
'''

#Int
-23435325

#Float
4.0 #adds a level of precision to 4

#String
"This is a string"
'This is also a string'

#Bool
True
False


'''
PRINTING:
1 print statement prints all contents in 1 line
next print statement will print on next line
This happens because default delimiter in print is "\n"
we can change it
'''
print(4.0, 12, "this is a string", 'this is also a string')
print("This statement prints on next line")
print("\n")
print("This is a line", end="|")
print("This is next line")


'''
VARIABLES:
We can declare a variable without specifying datatype

var_value : Snake case is convention in python
'''

take_value = 'hello'
take_another = 'abhinav'
print(take_value, take_another)

# Allowed variable names: Hello, hello, hello_world, hello12
# Not allowed variable names : 0hello, hello;
# Only special character allowed in variable names is '_'


'''
INPUT
You can only specify string prompt to input statement
All values captured as string
'''

name = input("Please type your name: ")
age = input("Please input your age: ")
print("Hello", name, ", your age is ", age)
# type of variable age is string
print(type(age)) 

