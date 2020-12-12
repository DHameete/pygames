from pygame import math, draw
from math import inf, degrees, atan2
from ray import Ray

YELLOW = (200,200,100)

class Particle:

    def __init__(self, color, display):
        self.pos = math.Vector2(display[0]/3, display[1]/3)
        self.rays = []
        self.color = color
        self.angle = 0

        for angle in range(-30, 31, 1):
            self.rays.append(Ray(self.pos, angle, self.color))


    def show(self, surface):
        draw.circle(surface, self.color, self.pos, 10)
        for ray in self.rays:
            ray.show(surface)

    def look(self, surface, walls):
        prev = self.rays[0].pos
        for ray in self.rays:
            ray.rotate(self.angle)

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
                draw.polygon(surface, YELLOW, [prev, closest, self.pos])
                # draw.aaline(surface, YELLOW, self.pos, closest)
                prev = closest


    def update(self, display, dx, dy, mouse):
        # Rotate
        mouseX = mouse[0]
        mouseY = mouse[1]
        self.angle = degrees(atan2(-(mouseY-self.pos.y),(mouseX-self.pos.x)))
        
        # Translate
        x = self.pos.x + dx 
        y = self.pos.y + dy 
        if (x < 0 or x > display[0]):
            x = x - dx
        if (y < 0 or y > display[1]):
            y = y - dy            
        self.pos.update(x, y)
            
