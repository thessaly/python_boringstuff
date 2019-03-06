    # Creando funciones
# def hello():
#     print('Holiii')
#     print('Holiii')
#     print('Que tal?')
#
# hello()

# Con un argumento, name como parametro
# def hello(name):
#     print('Holi ' + name)
#
# print('dime tu nombre')
# name = input()
# hello(name)

##################

# Magic8ball
# import random
#
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidedly so'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'
#
# Una forma de hacerlo
# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)

# Una forma mas corta
# print(getAnswer(random.randint(1,9)))

#########################
# Keywords and arguments for print()
# print('hola')
# print('mundo')
#
# print('hola', end=', ')
# print('mundo')
#
# print('cat', 'dog', 'mice')
# print('cat', 'dog', 'mice', sep=', ')

#########################
# try and except

def funcion(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
