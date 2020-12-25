import pygame
from settings import *
from random import randint


class Spot:

    def __init__(self, r, c, w, h):
        self.r = r
        self.c = c

        self.width = w
        self.height = h

        self.f = 0
        self.g = 0
        self.h = 1000

        self.wall = False
        if randint(0,10) < 3:
            self.wall = True


        self.neighbors = []
        self.previous = None


    def show(self, surface, color = NEW_COLOR):
        if self.wall:
            pygame.draw.rect(surface, BLACK, (self.c * self.width, self.r * self.height, self.width-1, self.height-1))    
        else:
            pygame.draw.rect(surface, color, (self.c * self.width, self.r * self.height, self.width-1, self.height-1))

    
    def addNeighbors(self,neighbor):
        self.neighbors.append(neighbor)