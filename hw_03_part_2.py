import random
from random import randint

#Description: function is to generate a set of unique random numbers in the specified range

def get_numbers_ticket(min, max, quantity):
    result_list = set()
    if min >= 1 and max <= 1000:
        while len(result_list) != quantity:
            result_list.add(randint(min, max))
    print(sorted(list(result_list)))
    return sorted(list(result_list)) #if success returns list of sorted unique numbers, otherwise - empty list
    
#test the function:
get_numbers_ticket(10, 20, 5)
