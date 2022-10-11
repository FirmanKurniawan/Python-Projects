# Sudoku puzzle solver using recursion and backtracking
# Created by Santosh Vasisht

def checkCell(grid, row, col, digit):
    for i in range(0, 9):
        if grid[row][i] == digit or grid[i][col] == digit:
            return False
    
    r = (row//3) * 3
    c = (col//3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[r+i][c+j] == digit:
                return False

    return True

def solveSudoku(grid):
    for row in range(9):
        for col in range(9):
            if(grid[row][col] == 0):
                for n in range(1, 10):
                    if checkCell(grid, row, col, n):
                        grid[row][col] = n
                        solveSudoku(grid)
                        grid[row][col] = 0
                return grid
    display(grid)

def display(grid):
    for row in grid:
        print(*row)

sudoku = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

if __name__ == '__main__':
    solveSudoku(sudoku)
