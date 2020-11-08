import pygame
from pygame.locals import *
import sys, math

width = 800
height = 600

WHITE = (255, 255, 255)

class Vec2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def scale(self, s):
        self.x = self.x * s
        self.y = self.y * s

    def normalize(self):
        n = math.sqrt(self.x * self.x + self.y * self.y)
        self.x = self.x / n
        self.y = self.y / n


class Ray:

    def __init__(self, x, y):
        self.pos = Vec2D(x, y)
        self.dir = Vec2D(1, 0)
        # self.dir.scale(10)

    def lookAt(self, x, y):
        self.dir.x = x - self.pos.x
        self.dir.y = y - self.pos.y
        self.dir.normalize()

    def show(self, surface):
        start = (self.pos.x, self.pos.y)
        end = (self.pos.x + 10*self.dir.x, self.pos.y + 10* self.dir.y)
        pygame.draw.aaline(surface, WHITE, start, end, 1)

    def cast(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if(den == 0):
            return

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if (t > 0 and t < 1 and u > 0):
            pt = Vec2D(0,0)
            pt.x = x1 + t * (x2 - x1)
            pt.y = y1 + t * (y2 - y1)
            return pt
        else:
            return

class Wall:

    def __init__(self, x1, y1, x2, y2):
        self.a = Vec2D(x1, y1)
        self.b = Vec2D(x2, y2)

    def show(self, surface):
        start = (self.a.x, self.a.y)
        end = (self.b.x, self.b.y)
        pygame.draw.aaline(surface, WHITE, start, end, 1)


def main():

    # setup
    pygame.init()
    display = (width, height)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Raycasting")


    wall = Wall(500,200,650,400)
    ray = Ray(100, 300)

    # draw
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        displaysurface.fill((51, 51, 51))
        wall.show(displaysurface)
        ray.show(displaysurface)

        (mouseX, mouseY) = pygame.mouse.get_pos()

        ray.lookAt(mouseX, mouseY)

        pt = ray.cast(wall)
        if(pt):
            pygame.draw.circle(displaysurface, (255, 255, 255), (pt.x, pt.y), 4)

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()