from decimal import ROUND_FLOOR
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

    #creating empty matrix of 0 to allow easier coding of asigning values and identifying guess square with a -1 in y coord
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

    #creating a random permutation of the required values
    tempArr = list(range(1, difficulty + 1));
    random.shuffle(tempArr);

    #copying randomly generated values into gameGrid
    for i in range(difficulty):
        for j in range(difficulty):
            gameGrid[i + 1][j + 1].changeX(tempArr[(j + i) % 9]);
    
    #adding values for clues in game to appripriate entries
    temp = [];
    sum = 0;
    #initilizing temp array to all 0 values
    for i in range(difficulty):
        temp.append(0);
    #filling left and top border clue y and x values respectively
    for i in range(difficulty + 1):
        for j in range(difficulty + 1):
            #calculate value for left border clue in this row
            sum += gameGrid[i][j].x();
            #add this rows clue value to the column total
            temp[j] += gameGrid[i][j].x();
        gameGrid[i][0].changeY(sum);
        sum = 0;
    
    #store column totals into clue boxes in top edge x
    for i in range(difficulty + 1):
        gameGrid[0][i].changeX(temp[i]);
    
    #go through each middle clue in grid and calculate its clue nad total values
    ratio = ROUND_FLOOR((difficulty+1)/4);
    for i in range(ratio):
        for j in range(ratio):
            if (i != 0 or j != 0):
                if (i == 0):
                    sum = 0;
                    for k in range(3):
                        sum += gameGrid[4*i + k + 1][4*j].x();
                    gameGrid[4*i][4*j].changeX(sum);
                elif (j == 0):
                    sum = 0;
                    for k in range(3):
                        sum += gameGrid[4*i][4*j + k + 1].x();
                    gameGrid[4*i][4*j].changeY(sum);
                else:
                    #case where box needs both vertical and horizontal
                    sum = 0;
                    for k in range(3):
                        sum += gameGrid[4*i + k + 1][4*j].x();
                    gameGrid[4*i][4*j].changeX(sum);
                    sum = 0;
                    for k in range(3):
                        sum += gameGrid[4*i][4*j + k + 1].x();
                    gameGrid[4*i][4*j].changeY(sum);

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

    pygame.display.update();

    return tempArray;


def kenkenCreate(difficulty, screen):
    print("in development");