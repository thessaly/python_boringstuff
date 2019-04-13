#! /usr/bin/python3

# opens all .txt files in a folder
import os, glob, re

pattern = input('Enter string to search:\n')
user_pattern = re.compile(pattern)
print('\nSearch will be performed in directory: ' + os.getcwd() + '\n')

# searches for any line that matches a user-supplied regular expression
for file in glob.glob('*.txt'):
    text = open(file, encoding='utf-8')
    lines = text.readlines()
    for line in lines:
        mo = user_pattern.search(line)
        if mo is not None:
            line = line.encode('utf-8')
            print('In file \'' + file + '\':')
            print(line)



# prints results to the screen
