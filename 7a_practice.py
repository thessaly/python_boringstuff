#° /usr/bin/python3
# Strong password detection program

import re, getpass

print('Hi! Let\'s test how strong is your password.')

# regexes

uppercase_regex = re.compile(r'[A-Z]+')
lowercase_regex = re.compile(r'[a-z]+')
digit_regex = re.compile(r'\d+')

while True:
    # getpass prompts for pw without echoing
    password = getpass.getpass(prompt='Enter your password: ')
    mo_upper = uppercase_regex.search(password)
    mo_lower = lowercase_regex.search(password)
    mo_digit = digit_regex.search(password)

    if len(password) < 8:
        print('Your password should be at least 8 characters long.')
    elif mo_upper is None:
        print('Your password should have at least one uppercase character.')
    elif mo_lower is None:
        print('Your password should have at least one lowercase character.')
    elif mo_digit is None:
        print('Your password should have at least one digit.')
    else:
        print('Congratulations! That\'s a strong one.')
        break
