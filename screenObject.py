from pickle import TRUE
import pygame, sys, json, random;
from GUIcomponentFuncs import *;
from gameLoad import *;

class screenButton:
    def __init__(self, leftEdge, width, topEdge, height, leftText, rightText, borderSize, screen, difficulty):
        self.top = topEdge;
        self.height = height;
        self.left = leftEdge;
        self.width = width;
        self.leftTxt = leftText;
        self.rightTxt = rightText;
        self.scr = screen;
        self.bord = borderSize;
        self.diff = difficulty;
        self.dir = 1;

    def create(self):
        col = [];
        for i in range(3):
            col.append(random.randint(25, 255));
        
        self.object = GUIcompFcn(self.width, self.height, self.left, self.top, False, (col), self.scr, 1, True, (0, 0, 0), self.bord, True);

    def setDir(self, direction):
        self.dir = direction;

    def createK(self):
        self.object = GUIcompFcn(self.width, self.height, self.left, self.top, False, (255, 255, 255), self.scr, self.dir, self.bord, (0, 0, 0), 3, True);

#    def addTxt(self):
#        self.object;
    
    def move(self, x, y, gameGrid):
        #covering over previous button location to avoid issues
        cover = pygame.surface.Surface((960, 540));
        pygame.draw.rect(cover, (255, 255, 255), (0, 0, 960, 540));
        self.scr.blit(cover, (0, 0));

        #creating new position for button
        self.left = x - 0.5*self.width;
        self.top = y - 0.5*self.height;
        drawHanoi(self.scr, self.diff, gameGrid);
        pygame.display.update();

    def border(self, bordSiz):
        self.bord = bordSiz;
        self.object = self.create(self);

class point:
    def __init__(self):
        self.x = 0;
        self.y = 0;
    def changeX(self, xNew):
        self.x = xNew;
    def changeY(self, yNew):
        self.y = yNew;
    def x(self):
        return self.x;
    def y(self):
        return self.y;