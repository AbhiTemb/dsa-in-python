'''
PYTHON

Python is a dynamically typed language 
i.e. we don't need to specify type of the variable 
while declaring it

The types are inferred at runtime hence we can 
reassign a variable to any type different from it's previous type

'''
n = 0
n = "hello"

# Multiple assignments
a, b = 4, "avcd"
print(a, b)

# Increment
p = 1
p += 1
p = p + 1
# p++ Not allowed

# Absence of value
k = None
print(k)

# If statement
n = 1
if n > 2:
    pass
elif n < 2:
    pass
else:
    pass

# Logical operators are: and, or, not 
# Looping from i = 0 to i = 3
for i in range(1,4):
    print(i)

print('Reverse Loop')
# Step size is negative because we wanna traverse in reverse direction
for i in range(5,2,-1):
    print(i)

