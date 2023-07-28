'''
BINARY SEARCH:

A searching algorithm that searches in O(log n) time in a sorted list
'''

'''

'''

''' 
Step 1 : State the problem clearly 
State the problem clearly in abstract terms
We need to find out the given number in a decreasing order sorted list of numbers.
This is to be done in minimum number of operations or lookups
'''

# def locate_card(cards, query):
#     print(cards, query)
#     pass    

'''
Step 2: Come up with example inputs and outputs
Try to cover all edge cases
cards = [5,4,3,2,1]
query = 2
output = 3

We will write our test cases in form of dictionaries tests
Writing down all test cases helps us find out most answer if we don't know answer straightaway

Edge cases in the input
1. List may have repeating numbers
2. Query doesn't exist in the list
3. Query is first element in list
4. Query is last element in list
5. List is empty
'''
tests = []
tests.append({
    'input': {
        'cards':[13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7,
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [8,8,6,6,6,6,6,6,3,2,2,2,0,0,0],
        'query': 6
    },
    'output': 2
})

tests.append({
    'input': {
        'cards': [9,7,5,2,-9],
        'query': -9
    },
    'output': 4
})

# result = locate_card(**tests[0].input)

'''
Step 3: Come up with a correct solution for the problem. State it in plain english.

Firstly, come up with a correct solution. This solution is often a BRUTE force solution

Brute force solution:
Bob can simply turn over all the cards one by one, till he finds the given card. TC: O(n) solution
Steps:
1. Create a variable position = 0
2. Loop the entire list
3. If you find the given card, stop and save the index of list in position variable
4. Return the position if position remains unchanged return -1 implying that element was not found

This algorithm is actually the "Linear search algorithm"
'''

'''
Step 4: Implement the solution and test it using example inputs. Fix bugs, if any.
'''
print('Linear search')
def locate_card(cards, query):
    # initialise the variable that will store the position of desired card
    position = -1
    # loop the entire list 
    for i in range(len(cards)):
        # if the desired card is equal to current card then store the position
        if cards[i] == query: 
            position = i
            break
    # store the position of the card
    return position

for i, test in enumerate(tests):
    algo_answer = locate_card(**test['input'])
    if  algo_answer == test['output']:
        print(f'Test case{i} passed !')
    else:
        print(f'The following test case failed')
        print('INPUT', test['input'])
        print('OUTPUT', test['output'])
        print('YOUR ANSWER', algo_answer)

# You can skip brute force solution if you have less time
# You can just state the brute force solution in plain english to save time

'''
Step 5: Analyse the algorithm's complexity and identify inefficiencies if any
ie. find the optimal solution

We need a way to measure no. of list accesses to measure that if we have satisfied the condition of minimal turning of cards

Brute force:
n accesses in worst case

Optimal solution:
'''

'''
Complexity and big O notation

Complexity: It is the measure of amount of time or space required by an algorithm for an input of given size.
Time complexity is assumed to be for worst case usually

'''

'''
Step 6: Apply the right technique to overcome the inefficiency.

Binary search is the best approach
We have pivot in middle because with it we can eliminate half of the array, This is the maximum we can eliminate
'''

'''
Step 7: Come up with a correct solution for the problem. State it in plain english.
Algorithm:

1. Find the middle element of the array.
2. If the pivot matches our query, we can return the index
3. If pivot > query => element lies in 1st half of the array
4. If pivot < query => element lies in 2nd half of the array
5. If pivot goes out of bounds , element does not exist in the array
'''

'''
Step 8: Implement the solution and test it using any example inputs. Fix bugs, if any.
'''
print('Binary search')
def locate_cards_bin_se(cards, query):
    s = 0
    e = len(cards) - 1

    while s <= e:
        mid = (s+e) // 2
        if query == cards[mid]:
            if mid-1 > 0 and cards[mid-1] == cards[mid]:
                # turn left
                e = mid - 1
            else: 
                # element found
                return mid
        elif query > cards[mid]:
            # turn left
            e = mid - 1
        else: 
            # turn right
            s = mid + 1

    return -1

for i, test in enumerate(tests):
    algo_answer = locate_cards_bin_se(**test['input'])
    if  algo_answer == test['output']:
        print(f'Test case{i} passed !')
    else:
        print(f'The following test case failed')
        print('INPUT', test['input'])
        print('OUTPUT', test['output'])
        print('YOUR ANSWER', algo_answer)

'''
Step 9: Analyse the algorithm's complexity and identify inefficiencies, if any.

TC: O(log N)
SC: O(1)

Function inside function is called function closure
'''
