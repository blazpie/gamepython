import os
import sys
import tty
import termios
from re import match
from time import sleep


def create_hero():
    os.system('clear')

    hero = {'exp': 0, 
            'level': 1,
            'wisdom': 1,
            'charisma': 1,
            'mental_strength': 1,
            'alive': True,
            'armor': False, 
            'equipment': [] }

    print("\nYou have 10 points to divide between: "
          "\nwisdom, charisma and mental strength"
          "\nTo add type: 'w', 'c', 'm': ")

    for i in range(10):
        player_choice = ''
        while not match("^[wcm]$", player_choice):
            print("\n{} more points to divide.".format(10 - i))
            player_choice = getch().lower()
            if player_choice == "w":
                hero['wisdom'] += 1
            elif player_choice == "c":
                hero['charisma'] += 1
            elif player_choice == "m":
                hero['mental_strength'] += 1
            else:
                print("\nWRONG INPUT")
                sleep(1)
            os.system('clear')
            print("\nWisdom: {}".format(hero['wisdom']))
            print("Charisma: {}".format(hero['charisma']))
            print("Mental strength: {}".format(hero['mental_strength']))

    return hero


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


hero = create_hero()
print(hero)