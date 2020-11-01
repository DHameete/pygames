import pygame
from pygame import gfxdraw
from pygame.locals import *
import sys
import random
import math


width = 1600
height = 900
n = 200
r_max = 8
speed = 20

class Star:

    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.z = random.randint(0, width)

        self.pz = self.z

    def update(self):
        # pass
        self.z = self.z - speed
        if (self.z < 50):
            self.x = random.randint(0, width)
            self.y = random.randint(0, height)           
            self.z = width

            self.pz = self.z


    def draw(self, surface):

        # cast to center 
        sx = ((self.x - width/2) / self.z) * width 
        sy = ((self.y - height/2) / self.z) * height 

        # cast back for drawing
        sx = math.floor(sx + width/2)
        sy = math.floor(sy + height/2)

        # radius
        r = math.floor(- (r_max / width) * self.z + r_max)

        # draw star
        gfxdraw.aacircle(surface, sx, sy, r, (255, 255, 255))
        gfxdraw.filled_circle(surface, sx, sy, r, (255, 255, 255))

        # calculate previous location
        psx = math.floor(((self.x - width/2) / self.pz) * width + width/2)
        psy = math.floor(((self.y - height/2) / self.pz) * height + height/2)

        # draw linne
        pygame.draw.line(surface, (255, 255, 255), (psx, psy), (sx, sy), 1)

        # set current depth
        self.pz = (self.z + 2*speed)


def main():

    # setup
    pygame.init()
    display = (width, height)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Starfield")

    stars = [Star() for i in range(n)]

    # draw
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        displaysurface.fill((0,0,0))

        for star in stars:
            star.update()
            star.draw(displaysurface)

        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
    quit()