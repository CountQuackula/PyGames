#this is a function which creates the main menu
import sys, pygame, time, random;
pygame.init();
from GUIcomponentFuncs import *

def menuCreator(screen, buttonCount, buttonTexts):
    #covering over previous GUI screen to ensure no overlap between displays
    cover = pygame.surface.Surface((960, 540));
    pygame.draw.rect(cover, (255, 255, 255), (0, 0, 960, 540));
    screen.blit(cover, (0, 0));


    #initilizing ratio variable
    ratio = (3 * buttonCount) + 1;

    #creating the 3 option buttons on screen
    buttons = [];
    temp = [];
    for i in range(buttonCount):
        for j in range(3):
            temp.append(random.randint(25, 255));
        buttons.append(GUIcompFcn(1920/4, 540/ratio * 2, 1920/8, 540/ratio * ((3 * i) + 1), False, temp, screen, 1, True, (0, 0, 0), 4, 1));
        temp = [];
    #button1 = GUIcompFcn(1920/4, 54 * 2, 1920/8, 54, False, (255, 0, 255), screen, 1, True, (0, 0, 0), 4, 1);
    #button2 = GUIcompFcn(1920/4, 54 * 2, 1920/8, 54 * 4, False, (0, 255, 255), screen, 1, True, (0, 0, 0), 4, 1);
    #button3 = GUIcompFcn(1920/4, 54 * 2, 1920/8, 54 * 7, False, (255, 255, 0), screen, 1, True, (0, 0, 0), 4, 1);
    #add a list to store button objects with random colours

    #initilizing list that stores the boundries of the buttons
    boundries = [];

    #calculating the boundries of the buttons
    for i in range(buttonCount):
        #creating an empty row variable
        row = [];

        #filling the empty row variable with boundry values
        row.insert(0, 1920/8);
        row.insert(1, row[0] + 1920/4);
        row.insert(2, 540/ratio * (3 * i + 1));
        row.insert(3, (540/ratio) + row[2]);

        #adding row values intot he boundries list variable
        boundries.insert(i, row);
    
    #setting font and size for pyGame
    font = pygame.font.Font('freesansbold.ttf', round(540/ratio));

    #creating the text objects to blit over pygame.display
    textList = [];
    for i in range(buttonCount):
        textList.append(font.render(buttonTexts[i], True, (0, 0, 0)));
    #text1 = font.render('Tower of Hanoi', True, (0, 0, 0));
    #text2 = font.render('Kakuro', True, (0, 0, 0));
    #text3 = font.render('KenKen', True, (0, 0, 0,));

    #bliting text objects onto the buttons
    for i in range(buttonCount):
        screen.blit(textList[i], (boundries[i][0] + 10, boundries[i][2] + 10));
    #screen.blit(text1, (boundries[0][0] + 10, boundries[0][2] + 10));
    #screen.blit(text2, (boundries[1][0] + 10, boundries[1][2] + 10));
    #screen.blit(text3, (boundries[2][0] + 10, boundries[2][2] + 10));

    #initlizing while loop pointer blocks and menu selected lists
    pntr = GUIcompFcn(540/ratio, 130/ratio, boundries[0][0] - 67, boundries[0][3] - 65/ratio, False, (0, 0, 0), screen, 1, False, (0, 0, 0), 0, 1);
    #pnt1 = GUIcompFcn(540/((3 * buttonCount) + 1), 130/((3 * buttonCount) + 1), boundries[0][0] - 670/((3 * buttonCount) + 1), boundries[0][3] - 600/((3 * buttonCount) + 1), False, (0, 0, 0), screen, 1, False, (0, 0, 0), 0, 1);
    #pnt2 = GUIcompFcn(540/((3 * buttonCount) + 1), 130/((3 * buttonCount) + 1), boundries[1][0] - 670/((3 * buttonCount) + 1), boundries[1][3] - 600/((3 * buttonCount) + 1), False, (0, 0, 0), screen, 1, False, (0, 0, 0), 0, 0);
    #pnt3 = GUIcompFcn(540/((3 * buttonCount) + 1), 130/((3 * buttonCount) + 1), boundries[2][0] - 670/((3 * buttonCount) + 1), boundries[2][3] - 600/((3 * buttonCount) + 1), False, (0, 0, 0), screen, 1, False, (0, 0, 0), 0, 0);
    #add 1 object to use as pntr and reuse in diff posituions in blit

    blankPnter = GUIcompFcn(540/ratio, 130/ratio, 0, 0, False, (255, 255, 255), screen, 1, False, (0, 0, 0), 0, 0);
    
    pressedDown = [1];
    pressedUp = [buttonCount - 1];
    for i in range(buttonCount - 1):
        pressedDown.append((i + 2) % buttonCount);
        pressedUp.append(i);
    #pressedDown = (1, 2 , 0);
    #pressedUp = (2, 0, 1);
    pnterPosition = 0;
    #add better lists to store change of array location etc

    #adding pointer positions to boundries
    #pnterPost = [boundries[0][0] - 130/ratio, boundries[0][3] - 540/ratio, boundries[1][0] - 130/ratio, boundries[1][3] - 540/ratio];
    #boundries.insert(buttonCount + 1, pnterPost);
    #print(boundries);

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
                    screen.blit(blankPnter, (boundries[pnterPosition][0] - 67, boundries[pnterPosition][3] - 65/ratio));

                    #changing selected option           
                    pnterPosition = pressedDown[pnterPosition];
                elif event.key == pygame.K_UP:
                    #bliting over old pnter
                    screen.blit(blankPnter, (boundries[pnterPosition][0] - 67, boundries[pnterPosition][3] - 65/ratio));

                    #changing selected option
                    pnterPosition = pressedUp[pnterPosition];
                elif event.key == pygame.K_RETURN:
                    return pnterPosition;

            #updating screen if arrow keys pressed
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                #deteminig which pnter to apply to screen
                screen.blit(pntr, (boundries[pnterPosition][0] - 67, boundries[pnterPosition][3] - 65/ratio))
                #if pnterPosition == 0:
                    #screen.blit(pnt1, (boundries[0][0] - 670/ratio, boundries[0][3] - 600/ratio));
                #elif pnterPosition == 1:
                    #screen.blit(pnt2, (boundries[1][0] - 670/ratio, boundries[1][3] - 600/ratio));
                #elif pnterPosition == 2:
                    #screen.blit(pnt3, (boundries[2][0] - 670/ratio, boundries[2][3] - 600/ratio));

                #updating screen to show the new pnt position
                pygame.display.update();

