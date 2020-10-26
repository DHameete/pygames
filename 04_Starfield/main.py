import pygame
from pygame.locals import *
import sys
import random


width = 800
height = 600
n = 100



class Star:

    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.z  = random.randint(0, width)


    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.ellipse(surface, (255, 255, 255), (self.x, self.y, 8, 8))



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