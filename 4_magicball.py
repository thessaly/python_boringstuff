import random

messages = ['It is certain', 'It is decidedly so', 'Yes definitely', 'Reply hazy try again', 'Ask again later', 'Concentrate and ask again', 'My reply is no', 'Outlook not so good', 'Very doubtful']

# prints a message looking for a random index number between zero and the last index of the list
print(messages[random.randint(0, len(messages) - 1)])
