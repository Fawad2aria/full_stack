import random

'''
number = int(input('Input a number: '))
guess = random.randint(1, 100)
def guess_the_number(guess, number, minimum, maximum):
    while guess != number:
        print(f"Computer guessed {guess}")
        print(f"guess: {guess} number: {number}, minimum: {minimum}, maximum: {maximum}")
        if guess < number:
            print('Try again! Your guess is too smalll.')
            minimum = guess + 1
            guess = int(average(guess, maximum))+1
        elif guess > number:
            print(f"Try again! Your gueess is too big.")
            maximum = guess - 1
            guess = int(average(guess, minimum))
    print(f"Correct! the number is {guess}")
def average(a,b):
    return (a + b) / 2
guess_the_number(guess, number, 1, 100)
'''
#----------------------------------------------------------------------#
guess = random.randint(1, 100)
number = int(input('Enter a number: '))
def guess_the_number(guess, number, minimum, maximum):
    print(f'Computer guessed {guess}')
    if (guess == number):
        print(f"Correct! the number is {guess}!")
    elif guess < number:
        print(f"Try again! your guess is too small.")
        guess_the_number(int(average(guess, maximum))+1, number, guess+1, maximum)
    else:
        print(f"Try again! you guess is too big.")
        guess_the_number(int(average(guess, minimum)), number, minimum, guess-1)
def average(a,b):
    return (a + b) / 2
guess_the_number(guess, number, 1, 100)