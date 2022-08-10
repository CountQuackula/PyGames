#this is the main script where function calls and movement between menus will be determined
import sys, pygame, json;
pygame.init();
from GUIcomponentFuncs import *;
from menuCreator import *;
from gameCreate import *;
from screenObject import *;

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

#setting GUI heading to the users chosen game
if selection[0] == 0:
    #calling Tower of Hanoi menu
    pygame.display.set_caption("Tower of Hanoi");
elif selection[0] == 1:
    #calling Kakuro menu
    pygame.display.set_caption("Kakuro");
elif selection[0] == 2:
    #calling KenKen menu
    pygame.display.set_caption("KenKen");

#initilizing game difficulty and video settings to default states
difficulty = 5;
videoSettings = 5;
selection.append(0);

#awaiting user choice on game loading method
while True:
    #asking user to choose next step
    text = ["New Game", "Load Save", "Difficulty"];
    selection[1] = (menuCreator(screen, 3, text));
    print(selection);
    
    #loading difficulty or video settings menus for user to choose from
    if selection[1] == 2:
        difficulty = menuCreator(screen, 9, ["1", "2", "3", "4", "5", "6", "7", "8", "9"]) + 1;
    elif selection[1] == 3:
        videoSettings = menuCreator(screen, 9, ["1", "2", "3", "4", "5", "6", "7", "8", "9"]);
    else:
        break;

#generating new game or loading save based off user decision
if selection[0] == 0:
    gameGrid = towHanoi(difficulty);
elif selection[0] == 1:
    print("lmao")
elif selection [0] == 2:
    print("1");