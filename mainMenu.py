#this is a function which creates the main menu
import sys, pygame, time;
pygame.init();
from GUIcomponentFuncs import *

def mainMenu(screen):
    #creating the 3 option buttons on screen
    button1 = GUIcompFcn(1920/4, 54 * 2, 1920/8, 54, False, (255, 0, 255), screen, 1, True, (0, 0, 0), 4, 1);
    button2 = GUIcompFcn(1920/4, 54 * 2, 1920/8, 54 * 4, False, (0, 255, 255), screen, 1, True, (0, 0, 0), 4, 1);
    button3 = GUIcompFcn(1920/4, 54 * 2, 1920/8, 54 * 7, False, (255, 255, 0), screen, 1, True, (0, 0, 0), 4, 1);

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

    #initlizing while loop pointer blocks and menu selected lists
    pnt1 = GUIcompFcn(54, 13, boundries[0][0] - 67, boundries[0][3] - 60, False, (0, 0, 0), screen, 1, False, (0, 0, 0), 0, 1);
    pnt2 = GUIcompFcn(54, 13, boundries[1][0] - 67, boundries[1][3] - 60, False, (0, 0, 0), screen, 1, False, (0, 0, 0), 0, 0);
    pnt3 = GUIcompFcn(54, 13, boundries[2][0] - 67, boundries[2][3] - 60, False, (0, 0, 0), screen, 1, False, (0, 0, 0), 0, 0);
    blankPnter = GUIcompFcn(54, 13, 0, 0, False, (255, 255, 255), screen, 1, False, (0, 0, 0), 0, 0);
    pressedDown = (1, 2 , 0);
    pressedUp = (2, 0, 1);
    pnterPosition = 0;

    #adding pointer positions to boundries
    pnterPost = (boundries[0][0] - 13, boundries[0][3] - 54, boundries[1][0] - 13, boundries[1][3] - 54);
    boundries.insert(4, pnterPost);

    #displaying initilial state of mainMenu before user input detection
    pygame.display.update();

    #checking pyGame for mouse or keyboard input to select an option or to close the game
    while True:
        #clearing event stream to only get latest user input
        pygame.event.clear;
        pygame.event.wait;

        for event in pygame.event.get():
            #determining user input
            if event.type == pygame.QUIT:
                #closing GUI and terminating code
                pygame.quit();
                sys.exit();
            elif event.type == pygame.KEYDOWN: #checking if it was a key being pressed down
                if event.key == pygame.K_DOWN: #checking if down arrow key was pressed
                    #bliting over old pnter
                    screen.blit(blankPnter, (boundries[pnterPosition][0] - 67, boundries[pnterPosition][3] - 60));

                    #changing selected option           
                    pnterPosition = pressedDown[pnterPosition];
                elif event.key == pygame.K_UP:
                    #bliting over old pnter
                    screen.blit(blankPnter, (boundries[pnterPosition][0] - 67, boundries[pnterPosition][3] - 60));

                    #changing selected option
                    pnterPosition = pressedUp[pnterPosition];
                elif event.key == pygame.K_RETURN:
                    return pnterPosition;

            #updating screen if arrow keys pressed
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                #deteminig which pnter to apply to screen
                if pnterPosition == 0:
                    screen.blit(pnt1, (boundries[0][0] - 67, boundries[0][3] - 60));
                elif pnterPosition == 1:
                    screen.blit(pnt2, (boundries[1][0] - 67, boundries[1][3] - 60));
                elif pnterPosition == 2:
                    screen.blit(pnt3, (boundries[2][0] - 67, boundries[2][3] - 60));

                #updating screen to show the new pnt position
                pygame.display.update();

