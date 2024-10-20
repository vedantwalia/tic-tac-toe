import numpy as np
import pygame
import math

ROWS = 3
COLUMNS = 3

def mark(row, col, player):
    board[row][col] = player

def is_valid_mark(row, col):
    return board[row][col] == 0

board = np.zeros((ROWS, COLUMNS))

print(board)
mark(2,1,2)
print(board)
print(is_valid_mark(2,1))