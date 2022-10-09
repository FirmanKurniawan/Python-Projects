#Tic Tac Toe Game
#Created by Santosh Vasisht

import random
import time

def display_board(board):
    #Display the current state of the board and positions
    print('\n\t  Board\t\tPositions')
    for i in range(5):
        for k in range(2):
            print('\t', end = '')
            for j in range(5):
                if(i%2):
                    if(j%2):
                        print('+', end = ' ')
                    else:
                        print('-', end = ' ')
                else:
                    if(j%2):
                        print('|', end = ' ')
                    else:
                        if(k):
                            print(3*(i//2)+(j//2)+1, end = ' ')
                        else:
                            print(board[i//2][j//2], end = ' ')
        print()
    print()

def input_position():
    #Check for valid input
    while(True):
        ip = int(input("Enter a position (1-9): "))
        if(ip in free):
            break
        print("Invalid position\n")
    return ip

def input_level():
    #Check for valid input
    print("\nLevels\n1: Easy\n2: Medium\n3: Hard\n")
    while(True):
        ip = int(input("Choose a level (1-3): "))
        if(ip == 1):
            print("\tLevel Easy")
            break
        if(ip == 2):
            print("\tLevel Medium")
            break
        if(ip == 3):
            print("\tLevel Hard")
            break
        print("Invalid Level\n")
    return ip

def pick_pos():
    if(level > 1):
        if(level == 3):
            #Pick attacking position
            for i in range(len(match_table)):
                if(match_table[i][1] == 2):
                    for j in match_map.keys():
                        if((i in match_map[j]) and (j in free)):
                            return j
        #Pick defending position
        for i in range(len(match_table)):
            if(match_table[i][0] == 2):
                for j in match_map.keys():
                    if((i in match_map[j]) and (j in free)):
                        return j
    return random.choice(free)

#Start playing
play = 'y'
while(play == 'y'):
    #SETUP
    board = [[' ', ' ', ' '] for _ in range(3)] #current board state
    free = list(range(1, 10)) #available positions
    match_table = [[0, 0] for _ in range(8)] #3 row matches, 3 column matches, 2 diagonal matches for X and O
    match_map = { #maps the position to match in match_table
        1: (0, 3, 6),
        2: (0, 4),
        3: (0, 5, 7),
        4: (1, 3),
        5: (1, 4, 6, 7),
        6: (1, 5),
        7: (2, 3, 7),
        8: (2, 4),
        9: (2, 5, 6)
    }
    turn = random.choice([-1, 1]) #whose turn to play
    win = None #flag variable to continue playing till winner is found
    print("\n\tTIC TAC TOE")
    level = input_level()
    display_board(board)

    #GAMEPLAY
    while(win == None):
        #Continue playing till winner is found or it is a draw
        if(turn == 1):
            #Player's turn
            print("Your Turn")
            pos = input_position()
            free.remove(pos)

            #Change board state
            board[(pos - 1) // 3][(pos - 1) % 3] = 'X'
            display_board(board)

            #Update match_table
            matches = match_map[pos]
            for m in matches:
                match_table[m][0] += 1
        else:
            #Computer's turn
            print("Computer's turn")
            time.sleep(1) #computer thinking time
            pos = pick_pos()
            free.remove(pos)
            print("Computer picked position", pos)

            #Change board state
            board[(pos - 1) // 3][(pos - 1) % 3] = 'O'
            display_board(board)

            #Update match_table
            matches = match_map[pos]
            for m in matches:
                match_table[m][1] += 1
        
        #Check for win or draw
        if(len(free) == 0):
            win = 0 #draw match
        for i in range(len(match_table)):
            if(match_table[i][0] == 3 or match_table[i][1] == 3):
                win = turn #winner is found
                break
        turn *= -1 #next turn

    #GAMEOVER
    if(win == 1):
        print("\tYOU WIN!\n")
    elif(win == -1):
        print("\tCOMPUTER WINS!\n")
    else:
        print("\tIT IS A DRAW!\n")

    play = input('Do you want to play again? (y/n): ').lower()

#Exit
print("Thank you for playing Tic Tac Toe\n")