import time, pygame, sys, json;

def drawHanoi(screen, difficulty, gameGrid):
    for i in range(difficulty):
        for j in range(3):
            if gameGrid[0][i + 1][j] != 0:
                tempObj = gameGrid[1][i + 1][j];
                screen.blit(tempObj.object, (tempObj.left, tempObj.top));