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

# Optional matching: return even if a part isn't there with ?
bat_regex = re.compile(r'Bat(wo)?man')

mo1 = bat_regex.search('A sentence with Batman')
mo2 = bat_regex.search('A sentence with Batwoman')

mo1.group() # returns Batman
mo2.group() # returns Batwoman

# Zero or more matching with *
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowowoman')

mo1.group() # returns Batman
mo2.group() # returns Batwoman
mo3.group() # returns Batwowowowoman

# One or more matching with +
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowowoman')

mo1.group() # returns None
mo2.group() # returns Batwoman
mo3.group() # returns Batwowowowoman

# Matching Specific Repetitions with {}
ha_regex = re.compile(r'(Ha){3}') # matches 'HaHaHa' only

ha_regex = re.compile(r'(Ha){3,5}') # matches HaHaHa', 'HaHaHaHa' & 'HaHaHaHaHa'.

##### Python’s regexs are greedy by default: in ambiguous situations they will match the longest string possible #####

# Matching the non-greedy version (shorter first) with ?

nongreedy_Ha_Regex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group() # returns 'HaHaHa'

#### FIND ALL (as long as there are no groups in the regex, will return list, otherwise tuple) ####

phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone_regex.findall('Cell: 415-555-9999 Work: 212-555-0000') # returns ['415-555-9999', '212-555-0000']

### characters classes

# \d Any numeric digit from 0 to 9.
# \D  Any character that is not a numeric digit from 0 to 9.
# \w  Any letter, numeric digit, or the underscore character.
# \W  Any character that is not a letter, numeric digit, or the underscore character.
# \s  Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S  Any character that is not a space, tab, or newline.

xmas_regex = re.compile(r'\d+\s\w+') # matches text that has one or more numeric digits ( \d+), followed by a whitespace character ( \s), followed by one or more letter/digit/underscore characters (\w+)

# Can create own character class with []

vowel_regex = re.compile(r'[aeiouAEIOU0-9]') # matches vowels, upper or lower case and numbers 0 to 9

consonant_regex = re.compile(r'[^aeiouAEIOU]') # can make it negative with ^

begins_hello = re.compile(r'^Hello')
ends_hello = re.compile(r'Hello$')
whole_string_num = re.compile(r'^\d+$') # e.g., '12345xyz67890' would return None

# Wildcard . (only one character)

at_regex = re.compile(r'.at')
at_regex.findall('The cat in the hat sat on the flat mat.') # returns ['cat', 'hat', 'sat', 'lat', 'mat']

# Using .* for matching all

name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search('First Name: Al Last Name: Sweigart')
mo.group(1) # 'Al'
mo.group(2) # 'Sweigart'

# Matching Newlines with the Dot Character (DOTALL)

no_NL_regex = re.compile('.*')
no_NL_regex .search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group() # 'Serve the public trust.'

 nl_regex = re.compile('.*', re.DOTALL)
 nl_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group() # 'Serve the public trust.\nProtect the innocent.\nUphold the law.'

# Case-Insensitive Matching: pass re.I as second argument of re.compile

robocop = re.compile(r'robocop', re.I)

# Text substitution

names_regex = re.compile(r'Agent \w+')

names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.') # returns 'CENSORED gave the secret documents to CENSORED.'

agents_regex = re.compile(r'Agent (\w)\w*')
agents_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.') # returns 'A**** told C**** that E**** knew B**** was a double agent.'

# Manage complex regexs: pass re.verbose as second argument of re.compile, ignores # and ' ', also using multiple lines for readability

phone_regex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?)')

phone_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))?  # area code
(\s|-|\.)?  # separator
\d{3}  # first 3 digits
(\s|-|\.)  # separator
\d{4} # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?  # extension
)''', re.VERBOSE)

# re.compile only takes two arguments, but you can combine DOTALL, IGNORECASE and VERBOSE like this:

some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
