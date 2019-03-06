#! /usr/bin/python
# Practice - The Collatz sequence

def collatz(number):
        if number % 2 == 0:
            result = number // 2
            print(result)
            return result
        else:
            result = 3 * number + 1
            print(result)
            return result

print('give me a number')

while True:
    try:
        num = int(input())
        rta = collatz(num)
        break
    except ValueError:
        print('Enter an integer')


while rta != 1:
    rta = collatz(rta)
print('Good for Collatz')
