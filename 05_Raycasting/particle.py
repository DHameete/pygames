from pygame import math, draw
from math import inf
from ray import Ray

YELLOW = (200,200,100)

class Particle:

    def __init__(self, color):
        self.pos = math.Vector2(0, 0)
        self.rays = []
        self.color = color

        for angle in range(-30, 30, 1):
            self.rays.append(Ray(self.pos, angle, self.color))

    def show(self, surface):
        draw.circle(surface, self.color, self.pos, 10)
        for ray in self.rays:
            ray.show(surface)

    def look(self, walls, surface):
        prev = self.rays[0].pos
        for ray in self.rays:
            closest = None
            record = inf
            for wall in walls:
                pt = ray.cast(wall)
                if(pt):
                    d = self.pos.distance_to(pt)
                    if(d < record):
                        record = d
                        closest = pt
            if closest:
                draw.polygon(surface,YELLOW,[prev,closest,self.pos])
                # pygame.draw.aaline(surface, WHITE, self.pos, closest)
                prev = closest

    def update(self, x, y):
        self.pos.update(x, y)
