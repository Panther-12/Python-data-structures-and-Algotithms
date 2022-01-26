# from linear_search import locate_card
from Binary_search import locate_card


# list holding all test cases
tests =[]

#### DEFINE TEST CASES ####

# The query is almost at the middle
test1 = {
    'input':{
        'cards':[10,7,1],
        'query':7
    },
    'output':1
}
# The query is at the beginning of the list
test2 = {
    'input':{
        'cards':[13,10,7,2,1],
        'query':13
    },
    'output':0
}
# The query is at the end of the list
test3 = {
    'input':{
        'cards':[11,10,7,2,1],
        'query':1
    },
    'output':4
}
# add the test cases to the tests list
tests.append(test1)
tests.append(test2)
tests.append(test3)
## Testing the function using data ###

# Loop through the tests list and apply the function to each test case
def testFunc():
    for test in tests:
        results = locate_card(**test['input'])
        if bool(results == test['output']):
            print('Answer: {answer} \n Correct answer: {test_result} \n Conclusion: Passed'.format(answer=results,test_result=test['output']))
            print()
        else:
            print('Answer: {answer} \n Correct answer: {test_result} \n Conclusion: Failed'.format(answer=results,test_result=test['output']))
            print()


testFunc()