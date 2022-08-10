import pygame, sys, json;
from screenObject import *;
from GUIcomponentFuncs import *;

def towHanoi(difficulty):
    gameGrid = [];
    tempArray = [];
    temp = [0, 0, 0];
    tempArray.append(temp);

    for i in range(difficulty):
        temp = [i + 1];

        for j in range(2):
            temp.append(0);

        tempArray.append(temp);

    gameGrid.append(tempArray);
    #for checking array generating as desired
    print(gameGrid);

    #resetting temp variables to store screen objects instead
    temp = [];
    tempArray = [];

    #for i in range(difficulty):
    #    for j in range(3):


    return gameGrid;