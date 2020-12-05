import random

'''
counter = 10
while True:
    user = input('Guess a number between 1 - 10: ')
    user = int(user)
    counter -= 1
    if user == guess_rand:
        print(f'Correct! you guessed {counter} times')
        break
    else:
        print(f'Try a gain')
        if counter < 1:
            print('You finished all your moves')
            print('Goodbye, come back soon')
            break
    
'''
'''
counter = 0
while True:
    user = input('Guess a number between 1 - 10: ')
    user = int(user)
    counter += 1
    if user == guess_rand:
        print(f'Correct! you guessed {counter} times')
        break
    else:
        print(f'Try a gain')
        if counter < 1:
            print('You finished all your moves')
            print('Goodbye, come back soon')
            break
'''
guess_rand = random.randint(1, 10)
old_guess = int(input('Guess a number between 1 - 10: '))
counter = 0
while True:
    old_guess += current_guess
    old_guess.append(current_guess)
    # current_guess = int(input('Guess a number between 1 - 10: '))
    differance = abs(current_guess - guess_rand)
    # print(differance)
    differances = abs(old_guess - guess_rand)
    # print(differances)
    counter += 1
    if current_guess == guess_rand:
        print(f'Correct! you guessed {counter} times')
        break
    elif current_guess < guess_rand:
        print(f'Your guess "{current_guess}" is too low. "')
    elif current_guess > guess_rand:
        print(f'Your guess "{current_guess}" is too high')
    else:
        print(f'Try a gain')
        if counter < 1:
            print('You finished all your moves')
            print('Goodbye, come back soon')
            break
    if differance == guess_rand:
        print('good')
        break
    else:
        continue
    