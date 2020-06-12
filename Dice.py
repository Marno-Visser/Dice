import random

game_run = True
dice1 = 0
dice2 = 0

while game_run:
    game = input('Do you wanna roll a dice? type y/n')
    if game[0].lower() == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print('Dice 1: ' + str(dice1))
        print('Dice 2: ' + str(dice2))
        print('Total: ' + str(dice1 + dice2))
    else:
        print('Thank you for playing, come back soon.')
        game_run = False
