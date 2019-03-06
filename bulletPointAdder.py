#! /usr/bin/python3

import pyperclip

text = pyperclip.paste()

input = text.split('\n')

for i in range(len(input)):
    input[i] = '* ' + input[i]

# input = str(input)
bulleted = '\n'.join(input)
pyperclip.copy(bulleted)
