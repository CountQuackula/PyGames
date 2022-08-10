import pygame, sys, json;
from screenObject import *;
from GUIcomponentFuncs import *;

def towHanoiCreate(difficulty, screen):
    #covering over previous GUI screen to ensure no overlap between displays
    cover = pygame.surface.Surface((960, 540));
    pygame.draw.rect(cover, (255, 255, 255), (0, 0, 960, 540));
    screen.blit(cover, (0, 0));

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

    #adding created array layer to final return array
    gameGrid.append(tempArray);
    #for checking array generating as desired
    print(gameGrid);

    #resetting temp variables to store screen objects instead
    temp = [];
    tempArray = [];
    tempObj = 0;

    #creating and storing individual square objects into temp list
    for i in range(difficulty + 1):
        for j in range(3):
            if gameGrid[0][i][j] != 0:
                tempObj = screenButton(192*1.5 - (i*96)/difficulty, (i*192)/difficulty, 540/(difficulty+2) * i, 540/(difficulty + 2), str(gameGrid[0][i][j]), "", 4, screen);
                tempObj.create();
                temp.append(tempObj);
            else:
                temp.append(0);
        tempArray.append(temp);
        temp = [];
    
    #adding temp list to second third dimension of game space
    gameGrid.append(tempArray);

    #updating display to reveal newly generated gmae space
    pygame.display.update();

    return gameGrid;

def kakuCreate():
    print("in development");