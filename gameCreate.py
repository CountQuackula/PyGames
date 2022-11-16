from random import randint, randrange
from tempfile import TemporaryDirectory
import pygame, sys, json, time;
from screenObject import *;
from GUIcomponentFuncs import *;
from itertools import permutations;

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

    #creating second matrix layer with blocks in place using first layer
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
    #gameGrid.append(tempArray);

    pygame.display.update();

    return tempArray;

def kakuCreate(difficulty, screen):
    print("in development");
    gameGrid = [];
    temp = [];
    tempArr = [];

    #creating empty matrix of 0 to allow easier coding of asigning values
    for i in range(difficulty + 1):
        for j in range(difficulty + 1):
            if (i == 0 or j == 0):
                temp.append(point());
            elif (i % 4 == 0 and j % 4 == 0):
                temp.append(point());
            else:
                temp.append(point());
                temp[j].changeY(-1);
        tempArr.append(temp);
        temp = [];

    #add the zeroed points to gameGrid as its first matrix layer
    gameGrid.append(tempArr);

    #creating all the permutations of required numbers
    l = list(permutations(range(1, difficulty + 1)));
    temp = [];

    #selecting a subset of permutations that make a valid matrix
    for i in range(difficulty):
        #selecting new random permutated row
        row = randint(0,len(l));
        rows = len(l);
        temp.append(l[row]);

        #removing each remaining permutated row that has a matching column entry
        for j in range(rows):
            for idx, (x, y) in enumerate(zip(temp[i], l[rows - 1 - j])):
                if x == y:
                    l.pop(rows - 1 - j);
                    break;

    #assigning values to gameGrid entries
    for i in range(difficulty):
        for j in range(difficulty):
            if (i % 4 == 0 and j % 4 == 0):
                gameGrid[i + 1][j + 1];
            else:
                gameGrid[i + 1][j + 1].changeX(temp[i][j]);
    
    #adding values for clues in game to appripriate entries
    for i in range(difficulty + 1):
        for j in range(difficulty + 1):
            if (i == 0):
                gameGrid[i][j];
            elif (j == 0):
                gameGrid[i][j];
            elif (i % 4 == 0 and j % 4 == 0):
                gameGrid[i][j];
            print("");

    gameGrid.append(loadKaku(gameGrid, screen, difficulty));

    return gameGrid;

def loadKaku(gameGrid, screen, difficulty):
    #covering over previous GUI screen to ensure no overlap between displays
    cover = pygame.surface.Surface((960, 540));
    pygame.draw.rect(cover, (255, 255, 255), (0, 0, 960, 540));
    screen.blit(cover, (0, 0));

    #
    temp = [];
    tempArray = [];
    tempObj = 0;
    for i in range(difficulty + 1):
        for j in range(difficulty + 1):
            if gameGrid[i][j].y() != -1:
                tempObj = screenButton(210 + (i*540/(difficulty + 1)), 540/(difficulty + 1), j*(540/(difficulty + 1)), 540/(difficulty + 1), str(gameGrid[i][j].x()), str(gameGrid[i][j].y()), 3, screen, difficulty);
                tempObj.setDir(0);
                tempObj.createK();
            else:
                tempObj = screenButton(210 + (i*540/(difficulty + 1)), 540/(difficulty + 1), j*(540/(difficulty + 1)), 540/(difficulty + 1), "", "", 3, screen, difficulty);
                tempObj.createK();

            temp.append(tempObj);
        tempArray.append(temp);
        temp = [];

    return tempArray;


def kenkenCreate(difficulty, screen):
    print("in development");