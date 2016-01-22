####################################################################
#
#    Alexander M. Thompson
#    CS 150, Project 3
#    Due September 28, 2013
#
#    This file is an implemenation of the classic snake game.
#
###################################################################

import random
from List import *
import os
import math

def main():
    board = generateMatrix(20, 30)    
    os.system('clear')
    player = [5,5]
    snake = [[15,15],[15,16],[15,17]]
    board[snake[0][0]][snake[0][1]] = "X"
    board[player[0]][player[1]] = "i"
    board[snake[1][0]][snake[1][1]] = "X"
    board[snake[2][0]][snake[2][1]]= "X"
    displayMatrix(board)
    tries = 0
    while(board[player[0]][player[1]] != "X"):
       os.system('clear')
       displayMatrix(board)
       print("Moves Taken: ", tries)
       mo = input("Enter a letter:")
       if (movePerson(mo, board, player) == True):
         moveSnake(snake, player, board)
         tries += 1
         if(tries > 0 and tries % 5 == 0):
           growingSnake(snake, board)
    os.system('clear')
    board[player[0]][player[1]] = "X"
    displayMatrix(board)
    print("You lose!")
    print("Final score:", tries)
    

def movePerson(mo, board, player):
    if(mo == 'j'): 
      if(1 <= player[1] <= 29):
        board[player[0]][player[1]] = "_"
        player[1] -= 1
        board[player[0]][player[1]] = "i"
        return True
    elif(mo == 'k'):
      if(0 <= player[1] <= 28):
        board[player[0]][player[1]] = "_"
        player[1] += 1
        board[player[0]][player[1]] = "i"
        return True
    elif(mo == 'i'):
      if(1 <= player[0] <= 20):
        board[player[0]][player[1]] = "_"
        player[0] -= 1
        board[player[0]][player[1]] = "i"
        return True
    elif(mo == 'm'):
      if(0 <= player[0] <= 18):
        board[player[0]][player[1]] = "_"
        player[0] += 1
        board[player[0]][player[1]] = "i"
        return True
    else:
      return None

def moveSnake(snake, player, board):
    surroundingsnake = [[snake[0][0] -1, snake[0][1]], [snake[0][0] +1, snake[0][1]], [snake[0][0], snake[0][1] -1], [snake[0][0], snake[0][1] +1], [snake[0][0] -1, snake[0][1] -1], [snake[0][0] + 1, snake[0][1] +1], [snake[0][0] -1, snake[0][1] +1], [snake[0][0] +1, snake[0][1] -1]]
    validHead = []
    for i in surroundingsnake: 
       if (0 <= i[1] <= 29 and 0 <= i[0] <= 19 and board[i[0]][i[1]] == "_" or board[i[0]][i[1]] == "i"): 
         validHead.append(i)
    iSmallest = 0
    iSmallest = distanceFunction(validHead, player, iSmallest)
    snake.insert(0, validHead[iSmallest])
    board[snake[0][0]][snake[0][1]] = "X" 
    board[snake[-1][0]][snake[-1][1]] = "_" 
    snake.pop()

def distanceFunction(array, player, index):
    distances = []
    for i in array:
        distances += [math.sqrt(((player[0] - i[0]) ** 2) + ((player[1] - i[1]) ** 2))]
    for i in range(1, len(distances), 1):
        if (distances[i] < distances[index]):
            index = i
    return index
    
def growingSnake(snake, board):
    surrounding = [[snake[-1][0] -1, snake[-1][1]], [snake[-1][0] + 1, snake[-1][1]], [snake[-1][0], snake[-1][1] - 1], [snake[-1][0], snake[-1][1] + 1]]
    vTail = []
    for i in surrounding:
       if((0 <= i[1] <= 29) and (0 <= i[0] <= 19) and board[i[0]][i[1]] == "_"):
         vTail.append(i)
    appendT = random.choice(vTail)
    snake.append(appendT)
    board[appendT[0]][appendT[1]] = "X"

def generateRow(cols):
    arr = []
    for i in range(0, cols, 1):
        arr += "_" 
    return arr

def generateMatrix(rows, cols):
    mat = []
    for i in range(0, rows, 1): 
        mat += [generateRow(cols)]
    return mat

def displayMatrix(mat):
    for i in range(0, len(mat), 1):
        for j in range(0, len(mat[i]), 1):
            print(mat[i][j], end = ' ')      
        print()

main()


