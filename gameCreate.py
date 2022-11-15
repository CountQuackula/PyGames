from random import randint, randrange
import pygame, sys, json, time;
from screenObject import *;
from GUIcomponentFuncs import *;

def towHanoiCreate(difficulty, screen):
    #initilizing temp lists and return list
    gameGrid = [];
    tempArray = [];
    temp = [0, 0, 0];
    tempArray.append(temp);

    #filling temp array with numerical values for positions of blocks
    for i in range(difficulty):
        temp = [i + 1];

        for j in range(2):
            temp.append(0);

        tempArray.append(temp);

    temp = [10, 10, 10];
    tempArray.append(temp);
    
    #adding created array layer to final return array
    gameGrid.append(tempArray);

    #resetting temp variables to store screen objects instead
    temp = [];
    tempArray = [];
    tempObj = 0;
    
    #adding temp list to second third dimension of game space
    gameGrid.append(hanoiLoad(gameGrid, screen, difficulty));

    return gameGrid;

def hanoiLoad(gameGrid, screen, difficulty):
    #covering over previous GUI screen to ensure no overlap between displays
    cover = pygame.surface.Surface((960, 540));
    pygame.draw.rect(cover, (255, 255, 255), (0, 0, 960, 540));
    screen.blit(cover, (0, 0));

    tempArray = [];
    temp = [];
    tempObj = 0;
    for i in range(difficulty + 1):
        for j in range(3):
            if gameGrid[0][i][j] != 0:
                tempObj = screenButton(192*(1.5 + j) - (gameGrid[0][i][j]*96)/difficulty, (gameGrid[0][i][j]*192)/difficulty, 540/(difficulty+3) * (i + 1), 540/(difficulty + 3), str(gameGrid[0][i][j]), "", 2, screen, difficulty);
                tempObj.create();
                temp.append(tempObj);
            else:
                temp.append(10);
        tempArray.append(temp);
        temp = [];
    
    #adding temp list to second third dimension of game space
    gameGrid.append(tempArray);

    pygame.display.update();

    return gameGrid[1];

def kakuCreate(difficulty, screen):
    print("in development");
    gameGrid = [];
    temp = [];
    tempArr = [];

    #creating empty matrix of 0 to allow easier coding of asigning values
    for i in range(difficulty + 1):
        for j in range(difficulty + 1):
            temp.append(point())
        tempArr.append(temp);
        temp = [];
    gameGrid.append(tempArr);

    #assigning values to gameGrid entries
    for i in range(difficulty + 1):
        if (i % 3 == 0):
            print("");
        else:
            for j in range(difficulty + 1):
                temp2 = [point()];
                temp2_5 = list(range(1, 10));
                random.shuffle(temp2_5);
                temp2.append(temp2_5);
                gameGrid[i] = temp2;
            print("");

    gameGrid.append(loadKaku(gameGrid, screen, difficulty));

    return gameGrid;

def loadKaku(gameGrid, screen, difficulty):

    return gameGrid[1];


def kenkenCreate(difficulty, screen):
    print("in development");