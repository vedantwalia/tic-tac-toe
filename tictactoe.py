import numpy as np
import pygame
import math

ROWS = 3
COLUMNS = 3

def mark(row, col, player):
    board[row][col] = player

def is_valid_mark(row, col):
    return board[row][col] == 0

def is_board_full():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 0:
                return False
    return True

board = np.zeros((ROWS, COLUMNS))

game_over = False

Turn = 0

while not game_over:
    if Turn % 2 == 0:
        #Player 1 turn
        row = int(input("Player 1: Choose row number (0-2): "))
        col = int(input("Player 1: Choose col number (0-2): "))
        if is_valid_mark(row, col): # checking if an already selected square is playied again
            mark(row, col, 1) 
        else:
            Turn -= 1

    else:
        #Player 2 turn
        row = int(input("Player 2: Choose row number (0-2): "))
        col = int(input("Player 2: Choose col number (0-2): "))
        if is_valid_mark(row, col): # checking if an already selected square is playied again
            mark(row, col, 2) 
        else:
            Turn -= 1 

    Turn += 1
    print(board)