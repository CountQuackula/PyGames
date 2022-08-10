from turtle import left
import pygame, sys, json;
from GUIcomponentFuncs import *;

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
        self.object = GUIcompFcn(self.width, self.height, self.left, self.top, False, (255, 255, 255), self.scr, 1, True, (0, 0, 0), self.bord, 1);

#    def addTxt(self):
#        self.object;
    
    def move(self, screen, x, y, blank):
        screen.blit(blank, self.left, self.top);
        self.left = x;
        self.top = y;
        screen.blit(self.object, (self.left, self.top));

    def border(self, bordSiz):
        self.bord = bordSiz;
        self.object = self.create(self);