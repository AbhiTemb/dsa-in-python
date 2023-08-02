import time

# Here are different ways to find minimum element in Python:
# 1. Looping and comparing all elements

n = int(input("Enter the no. of elements: "))
L = []
for i in range(n):
    L.append(int(input()))

print("Your input list: ", L)

# 2. Input all characters at once into string and split all numbers

start = time.time()
nums = input("Enter all the list elements: ")
L = []
for num in nums.strip().split():
    L.append(int(num))

print("Here is your input list: ", L)
end = time.time()
print("Time taken", end - start)

# 3. Use try and catch block

nums = input("Enter all the list elements: \n")
L = []

try:
    while True:
        num = int(input())
        L.append(num)
except Exception:
    print("Here is your list", L)

# 4. Using List comprehensions
start = time.time()
print("Begin entering your elements: ")

L = [int(item) for item in input().split()]

print("Here is your list", L)
end = time.time()
print("Time taken", end - start)
