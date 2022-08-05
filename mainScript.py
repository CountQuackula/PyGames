#this is the main script where function calls and movement between menus will be determined
import sys, pygame, time
from turtle import screensize;
pygame.init();
from GUIcomponentFuncs import *
from mainMenu import *
from menuCreator import *

#creating a screen for program
screenSize = (1920/2, 1080/2);
screen = pygame.display.set_mode(screenSize);
pygame.display.set_caption("Simple PyGames by Faisal");
screen.fill((255,255,255));


#calling main menu to create it
textMainMenu = ["Tower Of Hanoi", "Kakuro", "KenKen"];
selection = menuCreator(screen, 3, textMainMenu);
print(selection);

#calling KenKen menu
text = ["1", "2", "3", "4"];
selection = menuCreator(screen, 4, text);
print(selection);