# This is a more optimal solution compared to linear search
# It works only with sorted lists

  ##### ALGORITHM DESCRIPTION #####

  # 1. Find the middle value in the list by adding the first and last elements and dividing by 2
  # 2. Check whether it is equal to the query and return true if so
  # 3. If not check whether it is less than the query and in this case eliminate the right hand side of the list
  # 4. Set the highest value to the previous value in the list
  # 5. Also check whether the value is greater than the query and in this case eliminate the left hand side of the list
  # 6. Set the lowest value to the value after in the list


def locate_card(cards, query):
    lo, hi = 0, len(cards)
    # This loop ensures that the list is not empty
    while lo <= hi :
        # Average the sum of the lowest and highest points to get the mid point
        # Absolute division is used to eliminate errors from lists containing odd no of elements
        mid = (lo+hi)//2
        if cards [mid] == query:
            return mid
        elif cards[mid] < query:
            hi = mid-1
        elif cards[mid] > query:
            lo = mid + 1
    return print("mid position: {mid}  mid value: {value} query:{query}".format(mid=mid, value=cards[mid], query=query))

### ANALYZING ALGORITHM COMPLEXITY AND FIND INEFFICIENCY ####
   
   # The size of the array reduces to half in each iteration
   # iteration 1 -N
   # iteration 2 - N/2
   # iteration 3 - N/4 OR N/2v2
   # K Iterations = N/2 to power of k

    # Since the final length of the array is 1 N/2 to k = 1
    # Therefore n = 2 to k
    # log N = k ( log refers to base 2)

    # The big-o notation of this algorithm = O(logN) - ORDER LOG N


# FUNCTION CLOSURE- Writing a function inside a function
