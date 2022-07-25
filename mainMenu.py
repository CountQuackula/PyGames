#this is a function which creates the main menu
import sys, pygame, time;
pygame.init();
from GUIcomponentFuncs import *

def mainMenu(screen):
    #creating the 3 option buttons on screen
    button1 = GUIcompFcn(1920/4, 54 * 2, 1920/8, 54, False, (255, 0, 255), screen, 1, True, (0, 0, 0), 4);
    button2 = GUIcompFcn(1920/4, 54 * 2, 1920/8, 54 * 4, False, (0, 255, 255), screen, 1, True, (0, 0, 0), 4);
    button3 = GUIcompFcn(1920/4, 54 * 2, 1920/8, 54 * 7, False, (255, 255, 0), screen, 1, True, (0, 0, 0), 4);

    #updating screen to show the buttons added
    pygame.display.update();