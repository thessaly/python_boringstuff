#! /usr/bin/python3

# Use the pyperclip module to copy and paste strings.
import pyperclip, re

text = str(pyperclip.paste())


# Create two regexes, one for matching phone numbers and the other for matching email addresses.

phone_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))?  # area code (ddd or (ddd)), it's optional so ?
(\s|-|\.)?          # separator (can be ' ' or - or .)
(\d{3})             # first 3 digits
(\s|-|\.)           # separator
(\d{4})             # next 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension, ? optional, indicated by ' ' or ext or x or ext. plus 2-5 digits
)''', re.VERBOSE)

email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)


# Find all matches, not just the first match, of both regexes. Will return tuples.
matches = []
for groups in phone_regex.findall(text):
    phone = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':   # si hay una extension
        phone += ' x' + groups[8]
    matches.append(phone)

for groups in email_regex.findall(text):
    matches.append(groups[0])

# Display some kind of message if no matches were found in the text.
if not matches:
    print('Couldn\'t find any matches')

# Neatly format the matched strings into a single string to paste.
matches = '\n'.join(matches)
pyperclip.copy(matches)

print('Findings:')
print(matches)
print('Information copied to clipboard')
