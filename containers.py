import random as r

secret_number = r.randint(1,50)+1

guessed_number = int(input('Guess a number between 1 and 50: '))

while True:
    if guessed_number < secret_number:
        guessed_number = int(input(f'Guess a higher number than {guessed_number}: '))
    elif guessed_number > secret_number:
        guessed_number = int(input(f'Guess a smaller number than {guessed_number}: '))
    elif guessed_number == secret_number:
        print(f'YES! the secret number was {guessed_number}')
        break