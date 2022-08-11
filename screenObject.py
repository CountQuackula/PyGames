from turtle import left
import pygame, sys, json, random;
from GUIcomponentFuncs import *;
from gameLoad import *;

class screenButton:
    def __init__(self, leftEdge, width, topEdge, height, leftText, rightText, borderSize, screen):
        self.top = topEdge;
        self.height = height;
        self.left = leftEdge;
        self.width = width;
        self.leftTxt = leftText;
        self.rightTxt = rightText;
        self.scr = screen;
        self.bord = borderSize;

    def create(self):
        col = [];
        for i in range(3):
            col.append(random.randint(25, 255));
        
        self.object = GUIcompFcn(self.width, self.height, self.left, self.top, False, (col), self.scr, 1, True, (0, 0, 0), self.bord, True);

#    def addTxt(self):
#        self.object;
    
    def move(self, x, y):
        #covering over previous button location to avoid issues
        cover = pygame.surface.Surface((self.width + 1, self.height + 0.5));
        pygame.draw.rect(cover, (255, 255, 255), (0, 0, self.width + 1, self.height));
        self.scr.blit(cover, (self.left, self.top));

        #creating new position for button
        self.left = x - 0.5*self.width;
        self.top = y - 0.5*self.height;
        self.scr.blit(self.object, (self.left, self.top));
        pygame.display.update();

    def border(self, bordSiz):
        self.bord = bordSiz;
        self.object = self.create(self);