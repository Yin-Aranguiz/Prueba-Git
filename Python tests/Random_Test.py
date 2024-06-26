import random

randomNumber = random.randint(1,10)
guess = int(input('Take a guess: '))

while randomNumber != guess:
    print('Try again')
    guess=int(input('Take a guess: '))
print('You won!')