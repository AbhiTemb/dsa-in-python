'''
Q: Given an array of integers nums stored in ascending 
   order, find the starting and ending position of a given number
'''

'''
Step 1: State the problem clearly. Identify the i/p and o/p

The problem asks us to find first and last position of any element using binary search
i/p: lists of numbers arranged in descending order
o/p: list of two number corresponding to first and last position of given number
'''
'''
Step 2: Come up with sample inputs and outputs

i/p: [1, 2, 2, 3, 4, 4, 4, 5, 5] 4
o/p: [4, 6]

i/p: [1, 2, 3, 4, 5, 6, 8, 8, 8, 8] 8
o/p: [6, 9]

i/p: [3, 5, 8, 9] 0
o/p: [-1, -1]

i/p: [1, 2, 3, 4] 2
o/p: [1, 1]

i/p: [5, 5, 5, 5, 5, 5, 5, 5]
o/p: [0, 7]
'''

'''
Step 3 : Come up with a working solution , state steps only

Steps: 
We will implement upgraded binary search for both first and last position

These steps are finding first occurence
1. Take first and last pointer (s,e). Initialise it with first and last position
2. Pivot element should point to middle element.
3. If query == middle element then:
    3a. Check if same element exists left of current element
    3b. If yes, e = mid-1 and goto 2.
    3c. If no or no element exists on the left, This is the first occurence of desired element
4. If query < mid: e = mid-1 and goto step 2
5. If query > mid: s = mid+1 and goto step 2

These steps are finding last occurence
1. Take first and last pointer (s,e). Initialise it with first and last position
2. Pivot element should point to middle element.
3. If query == middle element then:
    3a. Check if same element exists right of current element
    3b. If yes, s = mid+1 and goto 2.
    3c. If no or no element exists on the right, This is the last occurence of desired element
4. If query < mid: e = mid-1 and goto step 2
5. If query > mid: s = mid+1 and goto step 2
'''


def first_occurence(numbers, query):
    s = 0
    e = len(numbers) - 1

    while s <= e:
        mid = (s + e) // 2
        if numbers[mid] == query :
            if mid == 0:
                return mid
            elif numbers[mid - 1] == numbers[mid]:
                e = mid - 1
            else:
                return mid
        elif numbers[mid] < query:
            s = mid + 1
        else: 
            e = mid - 1


def last_occurence(numbers, query):
    s = 0
    e = len(numbers) - 1

    while s <= e:
        mid = (s + e) // 2
        if numbers[mid] == query :
            if mid == len(numbers) - 1:
                return mid
            elif numbers[mid + 1] == numbers[mid]:
                s = mid + 1
            else:
                return mid
        elif numbers[mid] < query:
            s = mid + 1
        else: 
            e = mid - 1

def main():
    print("Please input size of array")        
    size = int(input())

    numbers = []
    for i in range(size):
        numbers.append(int(input("Input number: ")))

    print("Please enter the query:")
    query = int(input())
    
    answer = [first_occurence(numbers, query), last_occurence(numbers, query)]
    print("Answer", answer)

main()
