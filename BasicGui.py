#this is for testing and running basic pygame comamnds to create GUIs
import sys, pygame, time
pygame.init();
from GUIcomponentFuncs import *

#initilizing the GUI as a blank white 720p screen
sizeScreen = (1920/2, 1080/2);
screen = pygame.display.set_mode(sizeScreen);
screen.fill((255, 255, 255));

colours = (
    (1, 2, 3),
    (1, 3, 2),
    (3, 2, 1),
    (3, 1, 2),
    (2, 1, 3),
    (2, 3, 1),
);
position = (
    (0, 0),
    (1920/6, 0),
    (2*1920/6, 0),
    (0, 1080/4),
    (1920/6, 1080/4),
    (2*1920/6, 1080/4),
);

for k in range(6):
    block = GUIcompFcn(1920/6, 1080/4, position[k][0], position[k][1], True, colours[k], screen, 1, False, (0, 0, 0), 0);

#updating screen to show new added feature
pygame.display.update(); #updates the new image into the gui needs to be done after setting up a new image

time.sleep(10); #just pausing the ocde so the generated image can be appreciated

for k in range(6):
    blockTwo = GUIcompFcn(1920/12, 1080/2, k*1920/12, 0, True, colours[k], screen, -1, False, (0, 0, 0), 0);

#updating screen to show new added feature
pygame.display.update(); #updates the new image into the gui needs to be done after setting up a new image

time.sleep(10);