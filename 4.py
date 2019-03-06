# Lists
animales = ['cat', 'bat', 'dog']

animales[0]

# List of lists
spam = [['cat', 'bat', 'dog'], [10, 20, 30, 40, 50]]

# Should return 'bat'
print(spam[0][1])

# Should return 40
print(spam[1][3])

# Negative indexes start from the end (should return 'dog')
print(animales[-1])

# Slices are ranges, therefore also lists - They don't include upper limit
# Should return ['cat']
print(animales[0:1])

# Should return ['cat', 'bat']
print(animales[0:-1])

# Index zero can be replaced with empty value
# Should return ['cat']
print(animales[:1])

# Should return ['bat', 'dog']
print(animales[1:])

# Counting number of values in a list (returns 3)
print(len(animales))

# Assigning values to items in Lists
animales[1] = '12345'
print(animales)

# Operations with Lists
suma = animales + spam
print(suma)

mult = animales * 3
print(mult)

# Erasing a value
print(animales)
del animales[1]
print(animales)

# Iterating over indexes of a list
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# 'in' and 'not' operators

listita = ['hi', 'hey', 'hola', 'ho']
'hola' in listita  # returns True
'hola' not in listita # returns False

# The Multiple Assignment Trick: assign variables
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size)  # returns 'fat'

# Augmented Assignment Operators (can use with -, *, /, %)
julieta = 1
julieta += 1
print(julieta) #returns 2
