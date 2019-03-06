# Regular expressions (regexs)
# Try at https://www.regexpal.com/

import re # for regex always import re module

# If we're looking for the pattern telephone number: 544-698-7894 we can use \d{3}-\d{3}-\d{4}
# \d accounts for digit (0-9)

# It's convenient to pass raw strings (r') as regex due to escape characters
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # re.compile creates regex object to store the pattern

mo = phone_regex.search('Mi numero es 456-874-0253') # regex.search finds matches for the pattern, we store it in variable 'mo'

print('Numero de tel encontrado: ' + mo.group()) # re.group() returns found match objects if it's not 'None'

# Patterns can be grouped and returned in groups by using ()

phone_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phone_regex.search('Mi numero es 456-897-8957')

print('Numero encontrado: ' + mo.group()) # returns '456-897-8957'
print('Numero encontrado: ' + mo.group(1))  # returns 456
print('Numero encontrado: ' + mo.group(2)) # returns 897-8957

# Use it in plural to return all groups
mo.groups() # returns ('456', '897-8957')
area_code, main_number = mo.groups() # multiple assignment trick

# If pattern has parehthesis, they should be escaped:

phone_regex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

# A pipe means OR, returns first found

hero_regex = re.compile(r'Batman|Superman')
mo1 = hero_regex.search('Batman y su amigo Superman')
mo2 = hero_regex.search('Superman y su amigo Batman')

mo1.group() # returns Batman
mo2.group() # returns Superman

# Match one of several Patterns

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)') # pipe separates groups

mo = bat_regex.search('Batmobile lost a wheel')
mo.group() # returns Batmobile
mo.group(1) # returns mobile
