# # Dictionaries can use other values as indexes, which are called 'keys'
#
# my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'} # Dictionaries are defined by {key:value}
# my_cat['size'] # returns 'fat'
#
# # Order does not matter in a dictionary, therefore they can't be sliced
#
# spam = ['cats', 'dogs', 'moose']
# bacon = ['dogs', 'moose', 'cats']
# spam == bacon #returns False
#
# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# eggs == ham # returns True
#
# eggs['color'] # returns KeyError
#
# # Example with birthdays database
# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
#
# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break
#
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')
#
# ########################## DICTIONARY METHODS################################
# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
#
# for value in birthdays.values():
#     print(value) # returns only the dates
#
# for key in birthdays.keys():
#     print(key) # returns only the names
#
# for item in birthdays.items():
#     print(item) # returns the tuple for key:value pair
#
# # How to pass it into a list:
#
# agenda = list(birthdays.items())  # returns list [('Alice', 'Apr 1'), ('Bob', 'Dec 12'), ('Carol', 'Mar 4')]
#
# for k, v in birthdays.items():
#     print (k + ' birthday is on: ' + v + '. ')
#
# # Checking Whether a Key or Value Exists in a Dictionary
#
# 'Alice' in birthdays.keys() # True
# 'Julieta' not in birthdays.keys() # True
# 'Mar 4' in birthdays.values() # True
# 'Mar 4' in birthdays # returns false, by default searches for keys
#
# birthdays['Alice'] # returns 'Apr 1'
# birthdays['Julieta'] # returns KeyError
# birthdays.get('Julieta', 'No tengo ese nombre') # When key not found, returns specified value (or None if not specified)
#
# # Adding key and value if key is not there
#
# spam = {'name': 'Pooka', 'age': 5}
#
# spam.setdefault('color', 'black') # if there is no key 'color', sets value as 'black'. If key exists, returns current value.

###############################################################################
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
#
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# print(count)

############################# PRETTY PRINTING #########################################
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)

pprint.pprint(count) # Displays dictionary in a readable way, sorted
print(pprint.pformat(count)
