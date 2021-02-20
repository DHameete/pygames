import pygame, pygame.gfxdraw
import random

from settings import *

def f_line(x,y):
    # y = mx + b
    line1 = x + 0.5
    line2 = x - 0.5
    if line1 < y or line2 > y:
        label = 1
    else:
        label = 0

    return label

class Point:

    def __init__(self):
       
        self.x = random.uniform(-1,1)
        self.y = random.uniform(-1,1)
        self.bias = 1

        self.label = f_line(self.x, self.y)

    def pixelX(self):
        return (1 + self.x) / 2 * WIDTH

    def pixelY(self):
        return (1 - self.y) / 2 * HEIGHT

    def show(self, surface, color):
        px = self.pixelX()
        py = self.pixelY()

        if self.label > 0:
            # Square
            pygame.draw.rect(surface, color, (px, py, 8, 8))
        else:
            # Circle
            pygame.draw.circle(surface, color, (px, py), 5)
        
