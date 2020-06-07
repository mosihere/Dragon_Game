import random
import time

def displayIntro():
    print('You are in a land full dragons. in front of you')
    print('you see two caves. In one cave, the dragon is free')
    print('and will share his treasure with you. The other')
    print('Greedy and Hungry, and will eat you in a sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave !='2':
        print('which cave will you go into ? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave ...')
    time.sleep(2)
    print('it is dark and spooky ...')
    time.sleep(2)
    print('A large dragon jumps out in front of you ! he open ...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('his box, and Gives you his treasure!')
    else:
        print('his mouth, and Gobbles you down in one bite!')

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()