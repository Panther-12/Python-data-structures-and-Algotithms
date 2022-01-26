# John has 7 cards arranged in descending order. He is told to find card with the number 7. Write code that
# helps john find the card using few selections.

#### inputs ###
     # query - the number john is looking for
     # cards - a list of cards to select from

### output #####
     # The location of the card being sought after


####### sample input output ########

    # cards = [ 13,11,9,8,7,4,2]
    # query = 7
    # output = 4

##### Represent the test cases using dictionaries ########

    ## tests = []
    ## test1 = {
    #           'input':{
    #                   'cards':[13,11,9,8,7,4,2],
    #                    'query': 7
    #                   }
    #            'output':4
    #           }
    # tests.append(test1)

##### WRITE DOWN A SIGNATURE FUNCTION - Function that potrays the structure of the solution

    ## def locate_card(cards, query)
    ##      pass

##### List down edge cases ########

    ## The query is the first element
    ## The query is the last element
    ## The cards list is empty - return false
    ## The cards list contains only one element - if the element is the query return it else return false
    ## The query is almost at the middle of the cards list
    ## The query is a negative element
    ## The query is not in the cards list - return false
    ## Numbers or query repeat in the cards - return the first occurence of the query


#### come up with the correct solution. State it in plain english ######
#### correct solution is not an efficient solution. The most common solution is called the brute force solution ###

    ## In this case John can turn over the cards one after the other till he finds the card 

# Function that handles finding the positon of the query
def locate_card(cards, query):
    # Define starting positon
    position = 0
    # start a loop to allow checking each value in the cards list
    # Check to ensure the list is not empty
    while position < len(cards):
        # Check whether the card at that position is the query
        if cards[position] == query:
            return position
        # else increment the position by 1
        position +=1
        # check whether we are at the end of the list. If true return false else continue with the loop
        if position == len(cards):
            return False

