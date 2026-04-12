#Sebastian Siqueiros April 12, 2026. Module 3.2 Assignment
# This is a code for a Japanes dice game with the house fee increase from 10 to 12%

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

# CHANGE 1: Updated introduction to include bonus rule
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS RULE:
If you roll a total of 2 or 7, you receive a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        # CHANGE 2: Prompt changed to initials "ss:"
        pot = input('ss: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2  # Store total for bonus check

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    rollIsEven = total % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot

        # CHANGE 3: House fee changed from 10% → 12%
        print('The house collects a', int(pot * 0.12), 'mon fee.')
        purse = purse - int(pot * 0.12)

    else:
        purse = purse - pot
        print('You lost!')

    # CHANGE 4: Bonus logic for rolling 2 or 7
    if total == 2 or total == 7:
        print('Bonus! You rolled a total of', total, 'and earned 10 mon!')
        purse += 10

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()