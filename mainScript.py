#this is the main script where function calls and movement between menus will be determined
from statistics import harmonic_mean
import sys, pygame, json, time;
pygame.init();
from GUIcomponentFuncs import *;
from menuCreator import *;
from gameCreate import *;
from screenObject import *;
from gamePlay import *;

#creating a screen for program
screenSize = (1920/2, 1080/2);
screen = pygame.display.set_mode(screenSize);
pygame.display.set_caption("Simple PyGames by Faisal");
screen.fill((255,255,255));

#initilizing an empty list to store user selections
selection = [0, 0];

while True:
    #calling main menu to create it
    textMainMenu = ["Tower Of Hanoi", "Kakuro", "KenKen", "Exit Game"];
    selection[0] = menuCreator(screen, 4, textMainMenu);

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
    elif selection[0] == 3:
        pygame.quit;
        sys.exit();
    elif selection[0] == pygame.K_ESCAPE:
        pygame.quit;
        sys.exit();

    #initilizing game difficulty and chosen game to default states
    difficulty = 5;
    selection[1] = 0;

    #awaiting user choice on game loading method
    while True:
        #asking user to choose next step
        text = ["New Game", "Load Save", "Difficulty", "Back to Game Select"];
        selection[1] = (menuCreator(screen, 4, text));

        #generating new game or loading save based off user decision
        if selection[1] == 0:
            if selection[0] == 0:
                gameGrid = towHanoiCreate(difficulty, screen);
                playHanoi(difficulty, gameGrid, screen);
            elif selection[0] == 1:
                gameGrid = kakuCreate(difficulty, screen);
                playKakuro(difficulty, screen, gameGrid);
            elif selection [0] == 2:
                gameGrid = kenkenCreate(difficulty, screen);
                playKenKen(difficulty, screen, gameGrid);
        #loading up old game saves
        elif selection[1] == 1:
            if selection[0] == 0:
                print("load hanoi");
            elif selection[0] == 1:
                print("load kakuro");
            elif selection[0] == 2:
                print("load kenken");
        #loading difficulty or video settings menus for user to choose from
        elif selection[1] == 2:
            difficulty = menuCreator(screen, 9, ["1", "2", "3", "4", "5", "6", "7", "8", "9"]) + 1;
        #otherwise exiting code to return to main menu to select another game
        elif selection[1] == 3:
            break;
        elif selection[1] == pygame.K_ESCAPE:
            break;