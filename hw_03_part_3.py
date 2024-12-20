import re

# function recieves phone number in various formats and converts them to the fixed view

def normalize_phone(phone_number): # parameter is the string object in various formats
    cleaned_number = re.sub(r'\D', '', phone_number) #delete extra symbols from parameter
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number
    return cleaned_number #returns normalized phone number in fixed format: +380XXXXXXXXX

#CHECK THE FUNCTION
phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-99",
    "38050 111 22 33   "
]

sanitized_numbers = [normalize_phone(num) for num in phone_numbers]
print('Normalized phone numbers for sms sending:', sanitized_numbers)






# i tried to make it with creating list inside the function, so i got lists in list
# import re

# def normalize_phone(phone_number):
#     sanitized_numbers = []
#     cleaned_number = re.sub(r'\D', '', phone_number)
#     if not cleaned_number.startswith('+'):
#         if cleaned_number.startswith('380'):
#             sanitized_numbers.append('+' + cleaned_number)
#         else:
#             sanitized_numbers.append('+38' + cleaned_number)
#      return sanitized_numbers

# phone_numbers = [
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   "
# ]

# sanitized_numbers = [normalize_phone(num) for num in phone_numbers]
# print('Normalized phone numbers for sms sending:', sanitized_numbers)

