'''
CONTROL STRUCTURES:

while and for loops
for loops : allows us to iterate a set no. of times
while loops : allows us to iterate indeifinitely till the condition remains to be satisfied
'''

'''
For loops
i is iterator or count variable

range creates a collection of numbers, argument
range function arguments : start, stop, step
start: starts at that number
stop: stops BEFORE that number
step: skips step-1 number at each iteration 
'''
for i in range(10): 
    print(i, "This is a number")


for i in range(4, 18, 3):
    print(i, "this is a numbero")

print()
print()

# Won't work because i = start + n * step => i = -10 + -1 which is before -10 hence loop stops
for i in range(-10, -1, -1):
    print(i, "This is negative countdown")

print("list", list(range(0, 100, -1)))
# Range function stops if each iteration goes before start point
for i in range(0, -100, 1):
    print(i, "This is a never ending loop")

# We can iterate over all collections using for loop:
for i in (0, 1, 2, 3, 4): 
    print(i, "This is tuple element")

# If we want to loop index wise, here's what we do:
print("We are printing list")
L = [0, 45, 45, 234, 7450]
for i in range(len(L)):
    print(L[i])

# Or we can use enumerate function
for i, ele in enumerate(L):
    print(i, ele)

'''
While loops:
Will run the loop till condition is true and stops when condition is false
while condition == True:
    Do something
'''
i = 0
while i < 10:
    i += 1
    print("run", i)

# We can break out of closest loop using break statement
while i < 100:
    i *= 2
    print(i)
    while True:
        if i % 2 == 0:
            break
