import pygame
from settings import *


class Spot:

    def __init__(self, r, c, w, h):
        self.r = r
        self.c = c

        self.width = w
        self.height = h

        self.f = 0
        self.g = 0
        self.h = 0

        self.neighbors = []


    def show(self, surface, color = WHITE):
        pygame.draw.rect(surface, color, (self.c * self.width, self.r * self.height, self.width-1, self.height-1))

    
    def addNeighbors(self,neighbor):
        self.neighbors.append(neighbor)