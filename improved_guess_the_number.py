# Improvements to guess the number game

import random

def try_number(guess):

    if guess < secret_number:
        print('Your guess is too low.')
        return True
    elif guess > secret_number:
        print('Your guess is too high.')
        return True
    else:
        return False

secret_number = random.randint(1, 10)
guesses_taken = 0
print('I am thinking of a number between 1 and 10.')

# Ask the player to guess 9 times
while guesses_taken < 10:
    print('Take a guess.')
    
    try:
        guess = int(input())
        guesses_taken += 1
    except:
        print('Please enter a valid value.')
        continue

    if try_number(guess) == True:
        continue
    else:
        break

if guess == secret_number:
    print('Good job! You guessed my number in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret_number) + '.')
