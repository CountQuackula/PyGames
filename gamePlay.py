from contextlib import _GeneratorContextManager
from locale import currency
import pygame, sys, json;
from screenObject import *;
from GUIcomponentFuncs import *;

def playHanoi(difficulty, gameGrid):
    currCol = 0;
    left = [2, 0, 1];
    right = [1, 2, 0];
    picked = 0;
    tempObj = 0;
    tempNum = 0;
    while True:
        pygame.event.clear;
        pygame.event.wait;

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit;
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and picked == 0:
                    for i in range(difficulty + 1):
                        if gameGrid[0][i][currCol] != 0:
                            #copying object and its num value to temp variables
                            tempObj = gameGrid[1][i][currCol];
                            tempNum = gameGrid[0][i][currCol];

                            #setting the previous location for object to 0
                            gameGrid[1][i][currCol] = 0;
                            gameGrid[0][i][currCol] = 0;

                            #visually moving the object to the top row
                            tempObj.move(192 * (1.5 + currCol), 0.5*540/(difficulty + 3));
                            picked = 1;
                            break;
                elif event.key == pygame.K_RETURN and picked == 1:
                    for i in range(difficulty + 1):
                        if gameGrid[0][difficulty - i + 1][currCol] > tempNum and gameGrid[0][difficulty - i][currCol] == 0:
                            #visually moving the object to the top row
                            tempObj.move(192 * (1.5 + currCol), (1.5 + difficulty - i)*540/(difficulty + 3));
                            picked = 0;

                            #setting the previous location for object to 0
                            gameGrid[1][difficulty - i][currCol] = tempObj;
                            gameGrid[0][difficulty - i][currCol] = tempNum;
                            break;
                elif event.key == pygame.K_LEFT:
                    currCol = left[currCol];
                elif event.key == pygame.K_RIGHT:
                    currCol = right[currCol];
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit;
                    sys.exit();


def playKakuro(difficulty, screen, gameGrid):
    print("in development");

def playKenKen(difficulty, screen, gameGrid):
    print("in development");