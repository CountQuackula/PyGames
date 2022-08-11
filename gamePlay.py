from contextlib import _GeneratorContextManager
from locale import currency
from tempfile import TemporaryDirectory
import pygame, sys, json;
from menuCreator import *;
from screenObject import *;
from GUIcomponentFuncs import *;

def playHanoi(difficulty, gameGrid, screen):
    currCol = 0;
    left = [2, 0, 1];
    right = [1, 2, 0];
    picked = 0;
    tempObj = 0;
    tempNum = 0;
    pntr = GUIcompFcn(0.5*192, 0.25*540/(difficulty + 3), 192*1.25, 3*0.125*540/(difficulty + 3), False, (0, 0, 0), screen, 1, 0, (0, 0, 0), 0, True);
    blankPntr = GUIcompFcn(0.5*192, 0.25*540/(difficulty + 3), 192*1.25, 3*0.125*540/(difficulty + 3), False, (255, 255, 255), screen, 1, 0, (0, 0, 0), 0, False);
    pygame.display.update();
    while True:
        pygame.event.clear;
        pygame.event.wait;
        sum = 0;

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
                            tempRow = 0;
                            tempCol = currCol;

                            #setting the previous location for object to 0
                            gameGrid[1][i][currCol] = 0;
                            gameGrid[1][0][currCol] = tempObj;
                            gameGrid[0][i][currCol] = 0;
                            gameGrid[0][0][currCol] = tempNum;

                            #visually moving the object to the top row
                            tempObj.move(192 * (1.5 + currCol), 1.5*540/(difficulty + 3), gameGrid);
                            picked = 1;
                            screen.blit(pntr, (192 * (currCol + 1.25), 3*0.125*540/(difficulty + 3)));
                            pygame.display.update();
                            break;
                elif event.key == pygame.K_RETURN and picked == 1:
                    for i in range(difficulty + 1):
                        if gameGrid[0][difficulty - i + 1][currCol] > tempNum and gameGrid[0][difficulty - i][currCol] == 0:
                            #setting new values for old location of button
                            gameGrid[0][tempRow][tempCol] = 0;
                            gameGrid[1][tempRow][tempCol] = 0;

                            #setting the new location values for part
                            gameGrid[1][difficulty - i][currCol] = tempObj;
                            gameGrid[0][difficulty - i][currCol] = tempNum;

                            #visually moving the object to the top row
                            tempObj.move(192 * (1.5 + currCol), (1.5 + difficulty - i)*540/(difficulty + 3), gameGrid);
                            picked = 0;
                            screen.blit(pntr, (192 * (currCol + 1.25), 3*0.125*540/(difficulty + 3)));
                            pygame.display.update();
                            break;
                elif event.key == pygame.K_LEFT:
                    screen.blit(blankPntr, (192 * (currCol + 1.25), 3*0.125*540/(difficulty + 3)));
                    currCol = left[currCol];

                    #moving selected block if one is selected
                    if picked == 1:
                        #setting new values for old location of button
                        gameGrid[0][tempRow][tempCol] = 0;
                        gameGrid[1][tempRow][tempCol] = 0;

                        tempCol = currCol;

                        gameGrid[0][tempRow][tempCol] = tempNum;
                        gameGrid[1][tempRow][tempCol] = tempObj;

                        tempObj.move(192 * (1.5 + currCol), 1.5*540/(difficulty + 3), gameGrid);
                    
                    screen.blit(pntr, (192 * (currCol + 1.25), 3*0.125*540/(difficulty + 3)));
                    pygame.display.update();
                elif event.key == pygame.K_RIGHT:
                    screen.blit(blankPntr, (192 * (currCol + 1.25), 3*0.125*540/(difficulty + 3)));
                    currCol = right[currCol];

                    #moving selected block if one is selected
                    if picked == 1:
                        #setting new values for old location of button
                        gameGrid[0][tempRow][tempCol] = 0;
                        gameGrid[1][tempRow][tempCol] = 0;

                        tempCol = currCol;

                        gameGrid[0][tempRow][tempCol] = tempNum;
                        gameGrid[1][tempRow][tempCol] = tempObj;

                        tempObj.move(192 * (1.5 + currCol), 1.5*540/(difficulty + 3), gameGrid);
                    
                    screen.blit(pntr, (192 * (currCol + 1.25), 3*0.125*540/(difficulty + 3)));
                    pygame.display.update();
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_s:
                    #save(gameGrid->Hanoi.json);
                    print("save file");
                    return;

        for i in range(difficulty):
            sum += gameGrid[0][i + 1][2];
        
        if sum == difficulty*(difficulty + 1)/2:
            text = ["Won: back", "Won: exit"];
            opt = menuCreator(screen, 2, text);
            if opt == 0:
                break;
            elif opt == 1 or opt == pygame.K_ESCAPE:
                pygame.quit();
                sys.exit();


def playKakuro(difficulty, screen, gameGrid):
    print("in development");

def playKenKen(difficulty, screen, gameGrid):
    print("in development");