spam = ['apples', 'bananas', 'tofu', 'cats']
more_spam = [24, 56, 48, 59, 60]

def alguna(lista):
    string = ''
    for i in lista[0:len(spam)-1]:
        string = string + str(i) + ', '
    string = string + 'and ' + str(lista[len(lista)-1])
    return string

print('Lists to convert:')
print(spam)
print(more_spam)
print()
print('Strings:')
print(alguna(spam))
print(alguna(more_spam))
