import pygame
from pygame.locals import *
import sys, math, random

width = 800
height = 600

WHITE = (255, 255, 255)
YELLOW = (200,200,100)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

class Ray:

    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = pygame.math.Vector2(1, 0)
        self.dir = self.dir.rotate(angle)

    def lookAt(self, x, y):
        self.dir.x = x - self.pos.x
        self.dir.y = y - self.pos.y
        self.dir.normalize()

    def show(self, surface):
        end = self.pos + 10 * self.dir
        pygame.draw.aaline(surface, WHITE, self.pos, end, 1)

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
            pt = wall.a + t * (wall.b - wall.a)
            return pt
        else:
            return

class Wall:

    def __init__(self, x1, y1, x2, y2):
        self.a = pygame.math.Vector2(x1, y1)
        self.b = pygame.math.Vector2(x2, y2)

    def show(self, surface):
        pygame.draw.aaline(surface, BLUE, self.a, self.b, 1)

class Particle:

    def __init__(self):
        self.pos = pygame.math.Vector2(width/2, height/2)
        self.rays = []

        for angle in range(-30, 30, 1):
            self.rays.append(Ray(self.pos, angle))

    def show(self, surface):
        pygame.draw.circle(surface, WHITE, self.pos, 10)
        for ray in self.rays:
            ray.show(surface)

    def look(self, walls, surface):
        prev = self.rays[0].pos
        for ray in self.rays:
            closest = None
            record = math.inf
            for wall in walls:
                pt = ray.cast(wall)
                if(pt):
                    d = self.pos.distance_to(pt)
                    if(d < record):
                        record = d
                        closest = pt
            if closest:
                pygame.draw.polygon(surface,YELLOW,[prev,closest,self.pos])
                # pygame.draw.aaline(surface, WHITE, self.pos, closest)
                prev = closest

    def update(self, x, y):
        self.pos.update(x, y)


def main():

    # setup
    pygame.init()
    display = (width, height)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Raycasting")


    walls = []
    walls.append(Wall(0,0,width,0))
    walls.append(Wall(width,0,width,height))
    walls.append(Wall(width,height,0,height))
    walls.append(Wall(0,height,0,0))
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        walls.append(Wall(x1,y1,x2,y2))

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
        particle.look(walls, displaysurface)
        particle.show(displaysurface)

        for wall in walls:
            wall.show(displaysurface)

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()