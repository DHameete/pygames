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
        self.z = width

    def update(self):
        # pass
        self.z = self.z - 5

    def draw(self, surface):

        # cast to center and back
        sx = ((self.x - width/2) / self.z) * width + width/2
        sy = ((self.y - height/2) / self.z) * height + height/2

        pygame.draw.ellipse(surface, (255, 255, 255), (sx, sy, 8, 8))


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

        # tmpsurface = displaysurface.copy()
        # tmpsurface.fill((0, 100, 0))
        for star in stars:
            star.update()
            star.draw(displaysurface)

        # displaysurface.blit(tmpsurface, (width/2, height/2))

        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
    quit()