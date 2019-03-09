#! /usr/bin/python3
# regex version of strip()

# Takes a string, removes spaces beginning and end, if passed 2nd argument removes it tooself.
import re

word = str(input('Enter a string to strip: '))
symbol = str(input('If you want to remove other character than space, type it, if not type NO: '))

def regex_strip(string, character):
    regex = re.compile(r'(^\s\w+\s+$)|(\s+$)|(^\s)')
    regex_character = re.compile(str(character))
    mo = regex.search(string)
    if mo is None:
        if character != 'NO':
            print('Input has no spaces to remove, will remove input character: ' + character)
            string = regex_character.sub('', string)
        else:
            print('Input has no spaces to remove & you specified no character')
    else:
        regex_spaces = re.compile('\s')
        string = regex_spaces.sub('', string)
        if character != 'NO':
            string = regex_character.sub('', string)
    return print('Your final string is: \'' + string + '\'')

regex_strip(word, symbol)
