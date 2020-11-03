import pygame
from pygame.locals import *
import sys

width = 800
height = 600


class Vec2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Ray:

    def __init__(self):
            pass


class Boundary:

    def __init__(self, x1, y1, x2, y2):
        self.a = Vec2D(x1, y1)
        self.b = Vec2D(x2, y2)

    def show(self, surface):
        pygame.draw.line(surface, (255, 255, 255), (self.a.x, self.a.y), (self.b.x, self.b.y), 1)


def main():

    # setup
    pygame.init()
    display = (width, height)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Raycasting")
    B = Boundary(100,200,150,400)


    # draw
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        displaysurface.fill((51, 51, 51))
        B.show(displaysurface)

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()