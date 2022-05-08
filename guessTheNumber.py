# generate random number in 1 - 20 range and asks user to guess it untill successful
import random
secretNumber = random.randint(0, 20)
print('I\'m thinking of a number between 1 and 20.')
while True:
    print('Try to guess a number. ')
    guess = int(input())
    if guess == secretNumber:
        print('Good guess!')
        break
    elif guess < secretNumber:
        print('I\'m thinking of a higher number.')
    else:
        print('I\'m thinking of a lower number.')
