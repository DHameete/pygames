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

    def show(self, surface, color):
        if self.label >= 0:
            # Square
            pygame.draw.rect(surface, color, (self.x, self.y, 8, 8))
        else:
            # Circle
            pygame.draw.circle(surface, color, (self.x, self.y), 5)
        
