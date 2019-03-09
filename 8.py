## Writing and reading files

# File: path/file.extension to make the program work in any OS, must consider different notations

import os
os.path.join('usr', 'bin', 'spam') # returns string joined with character according to OS you're in

# windows --> usr\\bin\\spam (2 \ because of escape character)
# OS X, Linux --> usr/bin/spam

# Also works to print path of files:

my_files = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in myFiles:
    print(os.path.join('C:\\Users\\contaningfolder', filename))
    # returns C:\Users\asweigart\accounts.txt, C:\Users\asweigart\details.csv, C:\Users\asweigart\invite.docx

os.getcwd() # prints current working directory
os.chdir(/usr/documents) # changes cwd

# absolute and relative paths

os.getcwd() # returns /home/saynomore/Documentos/WORKSPACE/python_boringstuff
os.chdir('../')
os.getcwd() # returns /home/saynomore/Documentos/WORKSPACE
os.chdir('./palabras') # can also be just 'palabras'
os.getcwd() # returns /home/saynomore/Documentos/WORKSPACE/palabras

# create folders

os.makedirs('/home/saynomore/Documentos/WORKSPACE/new_folder/sarasa')

# The path module

os.path.abspath(path) # convert relative into absolute path
os.patch.isabs(path) # returns True if absolute, False if relative
os.path.relpath(path, start) # returns string of relative path from start, or if not provided, from cwd

path = '/home/saynomore/Documentos/WORKSPACE/python_boringstuff/7.py'
os.path.dirname(path) # returns '/home/saynomore/Documentos/WORKSPACE/python_boringstuff'
os.path.basename(path) # returns '7.py'
os.path.split(path) # returns tuple, not list: ('/home/saynomore/Documentos/WORKSPACE/python_boringstuff', '7.py')
path.split(os.path.sep) # returns list of items separated by separator according to running OS:

# File sizes
os.path.getsize(path) # returns size in bytes (6387)

# List of files in directory
os.listdir('..') # returns filenames for all files in that path

# Size of all files in a directory

size = 0

for file in os.listdir(os.getcwd()):
    size = size + os.path.getsize(os.path.join(os.getcwd(), file) # getsize needs whole path + filename

print(size)

# Checking path validity

os.path.exists(path) # True if it exists
os.path.isfile(path) # True if it's a file
os.path.isdir(path) # True if it's a folder

# For example, to check if there's a usb unit plugged:

os.path.exists('/home/mnt')

## File reading-writing process

# Creates file object, by default in reading mode
test = open('/home/saynomore/Documentos/testing.md')

text = test.read() # returns one sigle string with all content
lines = test.readlines() # returns list of strings, one for each line

# Creating in writing mode (overwrites) - if file doesn't exist it creates it

test = open('/home/saynomore/Documentos/testing.md', 'w')
test.write('escribo algo\n') # doesn't add line by itself

# Creating in append mode (adds to the end) - if file doesn't exist it creates it

test = open('/home/saynomore/Documentos/testing.md', 'a')
test.write('\n y agrego algo más')

# closing file everytime I wanna change mode
test.close()

############### SHELF FILES ###################
# Used for restore data to variables from the hard drive using shelf module

import shelve

# creates a shelf file
shelf_file = shelve.open('config')

# data to restore
data = ['uno', 'dos', 'tres']

# adding data to shelf file works like a dictionary
shelf_file['data'] = data

shelf_file.close() # 'config' file is created in the cwd, storing 'data'

# later, file can be reopened and data gathered
shelf_file = shelve.open('config')
new_variable = shelf_file['data'] # can use the data in this variable now
shelf_file.close()

# to bring shelf file keys & values:
keys = list(shelf_file.keys())
values = list(shelf_file.values())

# saving variables with pretty print: pprint.pformat(), which returns content as string
import pprint

cats = [{'name':'Otto', 'desc':'fluffy'}, {'name':'Layla', 'desc':'grumpy'}]

file_object = open('my_cats.py', 'w')
file_object.write('My cats are: ' + pprint.pformat(cats) + '\n')
file_object.close()

# now the file can be imported as a module

import my_cats
print(my_cats.cats) # returns [{'name':'Otto', 'desc':'fluffy'}, {'name':'Layla', 'desc':'grumpy'}]
print(my_cats.cats[0]) # returns {'name':'Otto', 'desc':'fluffy'}
print(my_cats.cats[0]['name']) # returns 'Otto'
