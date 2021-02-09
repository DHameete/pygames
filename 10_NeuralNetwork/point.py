import pygame, pygame.gfxdraw
import random

from settings import *

def f_line(x):
    # y = mx + b
    return 0.3 * x + 0.2

class Point:

    def __init__(self):
       
        self.x = random.uniform(-1,1)
        self.y = random.uniform(-1,1)
        self.bias = 1

        if f_line(self.x) > self.y:
            self.label = 1
        else:
            self.label = -1

    def pixelX(self):
        return (1 + self.x) / 2 * WIDTH

    def pixelY(self):
        return (1 - self.y) / 2 * HEIGHT

    def show(self, surface, color):
        px = self.pixelX()
        py = self.pixelY()

        if self.label >= 0:
            # Square
            pygame.draw.rect(surface, color, (px, py, 8, 8))
        else:
            # Circle
            pygame.draw.circle(surface, color, (px, py), 5)
        
