#! /usr/bin/python3
# Multiclipboard - Saves and loads pieces of text to the clipboard.
# .pyw extension means Python won’t show a Terminal window when running

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

# creates a shelve file to store the data
mcb_shelf = shelve.open('mcb')

# Save clipboard content:
# If the command line has 3 arguments and the 2nd one is 'save', load the 3rd one as key into the shelve file, and the clipboard as value
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.pop(sys.argv[2])
# Else, if the command line has two arguments
elif len(sys.argv) == 2:

# List available keywords
    if sys.argv[1].lower() == 'list':
        keys = list(mcb_shelf.keys())
        pyperclip.copy(str(keys))

# Load content to clipboard
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
