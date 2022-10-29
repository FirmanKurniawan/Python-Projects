#Importing tkinter and random library
from tkinter import *
from tkinter import messagebox
import random #Random library is needed so that each block's position is randomised each time

class Board:
    bg_color={ #Colours of each tile/block

        '2': '#f7f4f0',
        '4': '#ede0c8',
        '8': '#f5b867',
        '16': '#ed9013',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#f2b179',
        '1024': '#f59563',
        '2048': '#edc22e',
    } #Colours of the numbers - all set to black or white
    color={
         '2': '#0a0a0a',
        '4': '#0a0a0a',
        '8': '#0a0a0a',
        '16': '#0a0a0a',
        '32': '#f7f4f0',
        '64': '#f7f4f0',
        '128': '#f7f4f0',
        '256': '#f7f4f0',
        '512': '#f7f4f0',
        '1024': '#f7f4f0',
        '2048': '#f7f4f0',
    }
#function to start the game
    def __init__(game):
        game.window=Tk()
        game.window.title('2048 Game')
        game.gameArea=Frame(game.window,bg= 'azure3')
        game.board=[]
        game.gridCell=[[0]*4 for i in range(4)]
        game.compress=False
        game.merge=False
        game.moved=False
        game.score=0 #---All code above is before the game starts--

        for i in range(4):
            rows=[]
            for j in range(4):
                l=Label(game.gameArea,text='',bg='azure4',
                font=('arial',22,'bold'),width=4,height=2)
                l.grid(row=i,column=j,padx=7,pady=7)

                rows.append(l);
            game.board.append(rows)
        game.gameArea.grid() #Creates the grid of the game

        #Creating the matrix for the "game board"/ grid
        #--keeping track of all grid block that are empty or have a number
        #--Adding a 'number' block to the grid each time an event occurs
        
    def reverse(game):
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                game.gridCell[ind][i],game.gridCell[ind][j]=game.gridCell[ind][j],game.gridCell[ind][i]
                i+=1
                j-=1

    def transpose(game):
        game.gridCell=[list(t)for t in zip(*game.gridCell)]

    def compressGrid(game):
        game.compress=False
        temp=[[0] *4 for i in range(4)]
        for i in range(4):
            cnt=0
            for j in range(4):
                if game.gridCell[i][j]!=0:
                    temp[i][cnt]=game.gridCell[i][j]
                    if cnt!=j:
                        game.compress=True
                    cnt+=1
        game.gridCell=temp

#If you add (merge) the same number, the number is multiplied by 2
    def mergeGrid(game):
        game.merge=False
        for i in range(4):
            for j in range(4 - 1):
                if game.gridCell[i][j] == game.gridCell[i][j + 1] and game.gridCell[i][j] != 0:
                    game.gridCell[i][j] *= 2
                    game.gridCell[i][j + 1] = 0
                    game.score += game.gridCell[i][j]
                    game.merge = True

                    #Function to randomly add a new tile/number block
    def random_cell(game):
        cells=[]
        for i in range(4):
            for j in range(4):
                if game.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        game.gridCell[i][j]=2
    
    def can_merge(game):
        for i in range(4):
            for j in range(3):
                if game.gridCell[i][j] == game.gridCell[i][j+1]:
                    return True
        
        for i in range(3):
            for j in range(4):
                if game.gridCell[i+1][j] == game.gridCell[i][j]:
                    return True
        return False

    #Styling of the 'backgroud' grid
    def paintGrid(game):
        for i in range(4):
            for j in range(4):
                if game.gridCell[i][j]==0:
                    game.board[i][j].config(text='',bg='azure4')
                else:
                    game.board[i][j].config(text=str(game.gridCell[i][j]),
                    bg=game.bg_color.get(str(game.gridCell[i][j])),
                    fg=game.color.get(str(game.gridCell[i][j])))

#Init game by using the keyboard keys to move the tile/block 
#Directions: up, down, left, right

class Game:
    def __init__(game,gamepanel):
        game.gamepanel=gamepanel
        game.end=False
        game.won=False

    def start(game):
        game.gamepanel.random_cell()
        game.gamepanel.random_cell()
        game.gamepanel.paintGrid()
        game.gamepanel.window.bind('<Key>', game.link_keys)
        game.gamepanel.window.mainloop()
    
    def link_keys(game,event):
        if game.end or game.won:
            return

        game.gamepanel.compress = False
        game.gamepanel.merge = False
        game.gamepanel.moved = False

        presed_key=event.keysym

        if presed_key=='Up':
            game.gamepanel.transpose()
            game.gamepanel.compressGrid()
            game.gamepanel.mergeGrid()
            game.gamepanel.moved = game.gamepanel.compress or game.gamepanel.merge
            game.gamepanel.compressGrid()
            game.gamepanel.transpose()

        elif presed_key=='Down':
            game.gamepanel.transpose()
            game.gamepanel.reverse()
            game.gamepanel.compressGrid()
            game.gamepanel.mergeGrid()
            game.gamepanel.moved = game.gamepanel.compress or game.gamepanel.merge
            game.gamepanel.compressGrid()
            game.gamepanel.reverse()
            game.gamepanel.transpose()

        elif presed_key=='Left':
            game.gamepanel.compressGrid()
            game.gamepanel.mergeGrid()
            game.gamepanel.moved = game.gamepanel.compress or game.gamepanel.merge
            game.gamepanel.compressGrid()

        elif presed_key=='Right':
            game.gamepanel.reverse()
            game.gamepanel.compressGrid()
            game.gamepanel.mergeGrid()
            game.gamepanel.moved = game.gamepanel.compress or game.gamepanel.merge
            game.gamepanel.compressGrid()
            game.gamepanel.reverse()
        else:
            pass

        game.gamepanel.paintGrid()
        print(game.gamepanel.score)

    #If successfully managed to reach the number 2048
        flag=0
        for i in range(4):
            for j in range(4):
                if(game.gamepanel.gridCell[i][j]==2048):
                    flag=1
                    break

        if(flag==1): 
            game.won=True
            messagebox.showinfo('2048', message='You Won!!')
            print("won")
            return

        for i in range(4):
            for j in range(4):
                if game.gamepanel.gridCell[i][j]==0:
                    flag=1
                    break
#If you cannot make anymore moves and didnt reach 2048

        if not (flag or game.gamepanel.can_merge()):
            game.end=True
            messagebox.showinfo('2048','Game Over!!!')
            print("Over")

        if game.gamepanel.moved:
            game.gamepanel.random_cell()
        
        game.gamepanel.paintGrid()
    

gamepanel =Board()
game2048 = Game( gamepanel)
game2048.start()