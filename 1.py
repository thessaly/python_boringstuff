print('Hello world!')
print('Tell me your name')

my_name = input()

print('I love you, ' + my_name)
print()
print('The length of your name is: ')
print(len(my_name))

print('Tell me your age')

# input() always returns a string
my_age = input()

print('You will be: ' + str(int(my_age) + 1) + (' in a year.'))
