
name = ''

# Example of infinite loop
#while name != 'your name':
#    print('Please type your name.')
#    name = input()
#print('Thanks!')


# When used in conditions, 0, 0.0 and ' ' are considered False
# name = ''
# while not name:
#    print('Enter your name:')
#    name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests:
#    print('Be sure to have enough room for all your guests.')
# print('Done')


# # Gauss counter
# total = 0
# for num in range(101):
#     total = total + num
# print(total)


# Range can take three arguments: start, stop, step
# for i in range(0,10,2):
#     print(i)

# Steps can be negative
# for i in range(5,-1,-1):
    # print(i)


# Importing modules
# import random
# for i in range(5):
#     print(random.randint(1, 10))

# Can import multiple modules
# import random, sys, os, math

# Terminating a program
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed: ' + str(response) + '.')
