##### Strings

spam = "This is Alice's Cat"   # Using "" if text has ''

spam = 'O puedo usar un escape, this is Alice\'s cat'

print("Hello there!\nHow are you?\nI\'m doing fine.") # \n is new line, \t tab

print(r'O puedo usar un escape, this is Alice\'s cat') # the r makes it raw, returns all characters without escaping

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''') # Multiline strings take '''

# Strings can be sliced as lists

spam = 'Hola soy Otto!'

spam[:6] # returns 'Hola s'
signo = spam[-1] # returns '!'

# in and not in can be also used in Strings

'Hola' in spam # returns True
'hola' not in spam # returns True

######################## Useful strings METHODS ##############################

spam = spam.upper()  # returns spam = 'HOLA SOY OTTO!'
spam = spam.lower()  # returns spam = 'hola soy otto!'

# transforming to lower case can help with comparison of strings:
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

spam.isupper() # returns True if all characters are uppercase
spam.islower() # returns True if all characters are lowercase

# These methods can be chained:

'HELLO'.lower().islower() # returns True

# isX METHODS

'hello'.isalpha() # True (is letter?)
'hello456'.isalnum() # True (is letter or number?)
'hello'.isalnum() # True (is letter or number?)
'hello'.isdecimal() # False
'123456'.isdecimal() # True
' '.isspace() # True
'hello'.istitle() # False
'Hola Soy Otto!'.istitle() # True
'Hola Soy otto!'.istitle() # False

#### isX methods for input validation

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

### Checking parts of a string

'Hello world!'.startswith('Hello') # True
'Hello world!'.endswith('world!') # True
'abc123'.startswith('abcdef') # False
'abc123'.endswith('12') # False
'Hello world!'.startswith('Hello world!') # True
'Hello world!'.endswith('Hello world!') # True

### join(): call it on a string that glues items in a list:

' '.join(['Me', 'llamo', 'Julieta'])  # returns 'Me llamo Julieta'
', '.join(['cats', 'rats', 'bats']) # returns 'cats, rats, bats'

# split() does the opposite: call it on large string, specify delimiter

'My name is Simon'.split() # returns ['My', 'name', 'is', 'Simon'] (space by default)
'MyABCnameABCisABCSimon'.split('ABC') # returns ['My', 'name', 'is', 'Simon']

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''

spam.split('\n') # returns list with lines: ['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.', 'Sincerely,', 'Bob']

# Justifying text: justifies(total length of desired string, character to fill space as default)
#### See example 6_picnic.py

'Hello'.rjust(10)
# '     Hello'
'Hello'.rjust(20)
# '               Hello'
'Hello World'.rjust(20)
# '         Hello World'
'Hello'.ljust(10)
# 'Hello     '
'Hello'.rjust(20, '*')
# '***************Hello'
'Hello'.center(20)
# '       Hello        '
'Hello'.center(20, '=')
# '=======Hello========'

# Removing characters

spam = '       Hello World        '
spam.strip() # returns 'Hello World'
spam.lstrip() # returns 'Hello World      '
spam.rstrip() # returns '      Hello World'

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS') # specifying characters to strip, regardless order, returns 'BaconSpamEggs'

########## WORKING WITH THE CLIPBOARD

# module pyperclip must be installed first (sudo pip3 install pyperclip)

import pyperclip
pyperclip.copy('Hola soy Otto!')  # this copies to the clipboard
pyperclip.paste() # this pastes from the clipboard
