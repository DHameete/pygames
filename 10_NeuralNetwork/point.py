import pygame, pygame.gfxdraw
import random

from settings import *


class Point:

    def __init__(self):
        self.x = random.randrange(WIDTH)
        self.y = random.randrange(HEIGHT)
        
        if self.x > self.y:
            self.label = 1
        else:
            self.label = -1

    # def evaluate(self, p):
    #     self.label = p.guess((self.x,self.y))       

    def show(self, surface, color):
        if self.label >= 0:
            pygame.draw.rect(surface, color, (self.x, self.y,8,8))
        else:
            pygame.draw.circle(surface, color, (self.x, self.y), 5)
        
