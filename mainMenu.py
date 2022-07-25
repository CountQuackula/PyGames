#this is a function which creates the main menu
import sys, pygame, time;
pygame.init();
from GUIcomponentFuncs import *

def mainMenu(screen):
    #creating the 3 option buttons on screen
    button1 = GUIcompFcn(1920/4, 54 * 2, 1920/8, 54, False, (255, 0, 255), screen, 1, True, (0, 0, 0), 4);
    button2 = GUIcompFcn(1920/4, 54 * 2, 1920/8, 54 * 4, False, (0, 255, 255), screen, 1, True, (0, 0, 0), 4);
    button3 = GUIcompFcn(1920/4, 54 * 2, 1920/8, 54 * 7, False, (255, 255, 0), screen, 1, True, (0, 0, 0), 4);

    #initilizing list that stores the boundries of the buttons
    boundries = [];

    #calcualting the boundries of the buttons
    for i in range(3):
        #creating an empty row variable
        row = [];

        #filling the empty row variable with boundry values
        row.insert(0, 1920/8);
        row.insert(1, row[0] + 1920/4);
        row.insert(2, 54 * (3 * i + 1));
        row.insert(3, (54 * 2) + row[2]);

        #adding row values intot he boundries list variable
        boundries.insert(i, row);
    
    #setting font and size for pyGame
    font = pygame.font.Font('freesansbold.ttf', 54);

    #creating the text objects to blit over pygame.display
    text1 = font.render('Tower of Hanoi', True, (0, 0, 0));
    text2 = font.render('Kakuro', True, (0, 0, 0));
    text3 = font.render('KenKen', True, (0, 0, 0,));

    #bliting text objects onto the buttons
    screen.blit(text1, (boundries[0][0] + 48, boundries[0][2] + 27));
    screen.blit(text2, (boundries[1][0] + 144, boundries[1][2] + 27));
    screen.blit(text3, (boundries[2][0] + 144, boundries[2][2] + 27));

    #checking pyGame for mouse or keyboard input to select an option or to close the game


    #updating screen to show the buttons added
    pygame.display.update();

