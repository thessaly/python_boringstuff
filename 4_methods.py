# List methods - when running them in other data types, returns AttributeError

spam = ['hey', 'ho', 'lets', 'go', 'hey']

spam.index('ho') # returns 1
spam.index('hey') # returns zero, only first value encountered

spam.append('buh') # adds value in last place
spam.insert(1, 'bleh') # adds value in specified index
spam.remove('lets') # removes specified value from List - if value doesnt exist, returns ValueError
spam.remove('hey') # removes only first Value

more_spam = ['julieta', 'mariel', 'florencia', 'natalia', 'lucia']

more_spam.sort() # sorts ASCIIbetical or increasing # order, one data type at a time, *in place*
more_spam.sort(reverse=True) # sorts in reverse order
more_spam.sort(key=str.lower) # treats all values as lowercase, tricking ASCIIbetical into alphabetical

# With strings

nombre = 'Julieta'
nombre[0] # 'J'
nombre[0:5] # 'Juli'
nombre[-2] # 't'
'Ju' in nombre # True
'j' in nombre  # False
'J' not in nombre # False

# returns
# ***J***
# ***u***
# ***l***
# ***i***
# ***e***
# ***t***
# ***a***
for i in nombre:
    print('***' + i + '***')

# BUT: strings are immutable (cant change a letter for another, only slicing and making a new string), lists are mutable (we can add new values, delete, etc)

# Tuples: inmutable lists (good for ordered sequence that never changes & for optimizations)

tuple(more_spam) # returns ('julieta', 'mariel', 'florencia', 'natalia', 'lucia')
list(more_spam) # returns ['julieta', 'mariel', 'florencia', 'natalia', 'lucia']
list('Julieta') # returns ['J', 'u', 'l', 'i', 'e', 't', 'a']

# With strings, tuples and integer values (immutable), variables behave like this:

spam = 42
cheese = spam
spam = 100
spam # returns 100
cheese # returns 42

# But this mutable types like lists, Python uses references:

lista_a = ['uno', 'dos', 'tres', 'cuatro']
lista_b = lista_a
lista_b[1] = 'cinco'
lista_a # returns ['uno', 'cinco', 'tres', 'cuatro']

# Example: list spam is modified in place
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# To avoid this, I can use the module 'copy' and its functions, 'copy' and 'deepcopy':

import copy  # use deepcopy for lists with inner lists

lista_c = ['A', 'B', 'C', 'D']
lista_d = copy.copy(lista_c)
lista_d[1] = 24
print(lista_c) # returns ['A', 'B', 'C', 'D']
print(lista_d) # returns ['A', 24, 'C', 'D']
