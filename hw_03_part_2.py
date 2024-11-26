from random import randint


# Description: function is to generate a set of unique random numbers in the specified range

def get_numbers_ticket(min, max, quantity):
    result_list = set()
    if min >= 1 and (max - min +1) >= quantity and max <= 1000:
        while len(result_list) != quantity:
            result_list.add(randint(min, max))
    print(sorted(list(result_list)))
    return sorted(list(result_list))  # if success returns list of sorted unique numbers, otherwise - empty list


# test the function:

get_numbers_ticket(10, 10, 1)
get_numbers_ticket(1, 1000, 10)

# incorrect variants:
get_numbers_ticket(10, 4, 2) # (max_value is less than min_value)
get_numbers_ticket(10, 15, 9) # (quantity is higher than range)
get_numbers_ticket(10, 1001, 10) # (one of parameter is out of range)
