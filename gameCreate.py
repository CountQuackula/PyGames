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

    temp = [10, 10, 10];
    tempArray.append(temp);
    
    #adding created array layer to final return array
    gameGrid.append(tempArray);

    #resetting temp variables to store screen objects instead
    temp = [];
    tempArray = [];
    tempObj = 0;

    #creating and storing individual square objects into temp list
    for i in range(difficulty + 1):
        for j in range(3):
            if gameGrid[0][i][j] != 0:
                tempObj = screenButton(192*1.5 - (i*96)/difficulty, (i*192)/difficulty, 540/(difficulty+3) * (i + 1), 540/(difficulty + 3), str(gameGrid[0][i][j]), "", 2, screen, difficulty);
                tempObj.create();
                temp.append(tempObj);
            else:
                temp.append(10);
        tempArray.append(temp);
        temp = [];
    
    #adding temp list to second third dimension of game space
    gameGrid.append(tempArray);

    #updating display to reveal newly generated gmae space
    pygame.display.update();

    return gameGrid;

def kakuCreate(difficulty, screen):
    print("in development");
    

def kenkenCreate(difficulty, screen):
    print("in development");