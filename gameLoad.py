import time, pygame, sys, json;

def drawHanoi(screen, difficulty, gameGrid):
    for i in range(difficulty + 1):
        for j in range(3):
            if gameGrid[0][i][j] != 0:
                tempObj = gameGrid[1][i][j];
                screen.blit(tempObj.object, (tempObj.left, tempObj.top));