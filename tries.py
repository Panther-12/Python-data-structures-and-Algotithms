import unittest
from Binary_search import locate_card
from first_last import search_logic




class BinarySearch(unittest.TestCase):
	# Test cases
	def test_number(self):
		COUNT = 0
		PASSED = 0
		FAILED = 0
		CASE1 = [{
    		'input':{
        		'cards':[1,5,7,7,10],
        		'query':7
    		},
    		'output':2
		},{'input':{
        	'cards':[4,6,8,10,13,13,13,13,13,13],
        	'query':13
    		},
    		'output':4
		}]
		while COUNT < len(CASE1):
			result = search_logic(CASE1[COUNT]['input']['cards'], CASE1[COUNT]['input']['query'])
			if result == CASE1[COUNT]['output']:
				PASSED+=1
			else:
				FAILED+=1
			print('Result:',result,'\t Expected:',CASE1[COUNT]['output'])
			COUNT+=1
		return print('\n Number of tests:',COUNT,'\n PASSED:',PASSED,'\n FAILED:',FAILED)


if __name__ == '__main__':
	unittest.main()