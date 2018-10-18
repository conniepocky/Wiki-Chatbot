import random

guessesTaken = 0

print('Hi! What is your name?')
name = input()

number = random.randint(1, 20)
print(name + ' Try and guess my number that is between 1 and 100 :)')

while guessesTaken < 6:
    guess = int(input())

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low :0') 

    if guess > number:
        print('Your guess is too high :0')

    if guess == number:
        print('YAYYYYYYYYY! You did it! ')
        print()
        break

import menu