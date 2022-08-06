#this is the main script where function calls and movement between menus will be determined
import sys, pygame, time
from turtle import screensize;
pygame.init();
from GUIcomponentFuncs import *
from menuCreator import *

#creating a screen for program
screenSize = (1920/2, 1080/2);
screen = pygame.display.set_mode(screenSize);
pygame.display.set_caption("Simple PyGames by Faisal");
screen.fill((255,255,255));

#initilizing an empty list to store user selections
selection = [];

#calling main menu to create it
textMainMenu = ["Tower Of Hanoi", "Kakuro", "KenKen"];
selection.append(menuCreator(screen, 3, textMainMenu));
print(selection);

#
if selection[0] == 0:
    #calling Tower of Hanoi menu
    pygame.display.set_caption("Tower of Hanoi");
elif selection[0] == 1:
    #calling Kakuro menu
    pygame.display.set_caption("Kakuro");
elif selection[0] == 2:
    #calling KenKen menu
    pygame.display.set_caption("KenKen");

text = ["New Game", "Load Save", "Difficulty", "Video Settings"];
selection.append(menuCreator(screen, 4, text));
print(selection);