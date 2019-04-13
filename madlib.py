#! /usr/bin/python3
#  reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
# /home/saynomore/Documentos/probando2.txt
import re, os
# Ask for text file, print content
path = input('Hi, please enter path to text file:\n')
text_file = open(path)
content = text_file.read()

print('\nFile contains the following text:')
print(content)

# Look for ADJECTIVE, NOUN, ADVERB, VERB
while True:
    if 'ADJECTIVE' in content:
        print('Enter an adjective:')
        content = re.sub('ADJECTIVE',input(), str(content))
    elif 'NOUN' in content:
        print('Enter a noun:')
        content = re.sub(r'NOUN.*?',input(), str(content))
    elif 'ADVERB' in content:
        print('Enter an adverb:')
        content = re.sub('ADVERB',input(), str(content))
    elif 'VERB' in content:
        print('Enter a verb:')
        content = re.sub('VERB',input(), str(content))
    else:
        print('\nReplacement complete:')
        print(content)
        new_content = open('newcontent.txt', 'w')
        new_content.write(str(content))
        new_content.close()
        text_file.close()
        print('You can find your new text in: '+ os.getcwd() + '/newcontent.txt')
        break


# print result of replacement and save text to new file
