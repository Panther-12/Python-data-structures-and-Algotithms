
# Find the last and first position of a recurring element in an array
# SORTED LIST: This means the elements are arranged in ascending order

# Find the first position of an element in an array
def test_locations(cards,query,mid):
	mid_number = cards[mid]
	if mid_number == query:
		if mid-1 >=0 and cards[mid-1] == query:
			# If the last occurrence is required set return to left
			return 'right'
		return 'found'

	elif mid_number <query:
		return 'left'
	elif mid_number > query:
		return 'right'

def search_logic(cards,query):
	lo,hi = 0,len(cards)
	while lo<=hi:
		mid = (lo+hi)//2
		result = test_locations(cards=cards, query=query, mid=mid)
		if result == 'found':
			return mid
		elif result == 'left':
			lo = mid+1
		elif result == 'right':
			hi = mid-1
