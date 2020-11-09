import pygame
from pygame.locals import *
import sys, math, random

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
        r = math.sqrt(self.x * self.x + self.y * self.y)
        self.x = self.x / r
        self.y = self.y / r

    def rotate(self, angle):
        r = math.sqrt(self.x * self.x + self.y * self.y)
        self.x = r * math.cos(angle)
        self.y = r * math.sin(angle)


class Ray:

    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = Vec2D(1, 0)
        self.dir.rotate(angle)
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

class Particle:

    def __init__(self):
        self.pos = Vec2D(width/2, height/2)
        self.rays = []

        for angle in range(0, 360, 10):
            self.rays.append(Ray(self.pos, math.radians(angle)))

    def show(self, surface):
        pygame.draw.circle(surface, WHITE, (self.pos.x, self.pos.y), 10)
        for ray in self.rays:
            ray.show(surface)

    def look(self, wall, surface):
        for ray in self.rays:
            pt = ray.cast(wall)
            if(pt):
                pygame.draw.aaline(surface, WHITE, (self.pos.x, self.pos.y), (pt.x, pt.y))
                pygame.draw.circle(surface, WHITE, (pt.x, pt.y), 4)

    def update(self, x, y):
        self.pos.x = x
        self.pos.y = y


def main():

    # setup
    pygame.init()
    display = (width, height)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Raycasting")


    walls = []
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        walls.append(Wall(x1,x2,y1,y2))

    particle = Particle()

    # draw
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        displaysurface.fill((51, 51, 51))
        
        (mouseX, mouseY) = pygame.mouse.get_pos()
        particle.update(mouseX, mouseY)
        particle.show(displaysurface)

        for wall in walls:
            wall.show(displaysurface)
            particle.look(wall, displaysurface)

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()