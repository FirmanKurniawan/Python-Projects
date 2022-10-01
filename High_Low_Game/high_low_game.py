import random
from time import sleep

def win(s, h):  # if win
    for i in f"Your hint was {show}. The hidden number was {hide}\n":
        print(i, end='')
        sleep(0.04)
    for i in "You won!":
        print(i, end='')
        sleep(0.08)


def lost(s, h):  # if lost
    for i in f"Your hint was {show}. The hidden number was {hide}\n":
        print(i, end='')
        sleep(0.04)
    for i in "You lost!":
        print(i, end='')
        sleep(0.08)


def game(x):  # process of High - Low game
    if x == 'h':
        if hide > show:
            win(show, hide)
        else:
            lost(show, hide)
    elif x == 'l':
        if hide < show:
            win(show, hide)
        else:
            lost(show, hide)
    else:
        if hide == show:
            for i in f"Your hint and hidden number was a same number {show}.\n":
                print(i, end='')
                sleep(0.04)
            for i in "You won!":
                print(i, end='')
                sleep(0.08)
        else:
            lost(show, hide)


def checker(x):  # checking whether its 'h' or 'l' or 's'
    if x == 'h' or x == 'l' or x == 's':
        game(x)
    else:
        print("Enter 'h' or 'l' or 's' only")
        x = input().lower()
        checker(x)


hide = random.randint(1, 99)
show = random.randint(1, 99)
print("              HIGH - LOW GAME")
print("              ===============")
print("I just chose a secret number between 0 to 100")
sleep(1)
print()
print("Is the secret number higher or lower than {}?".format(show))
print()
sleep(1)
x = input("Enter 'h' if you think it's higher\nEnter 'l' if you think it's lower\nEnter 's' if you think it's the same\n").lower()
checker(x)
