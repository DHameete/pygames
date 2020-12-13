from pygame import math, draw
from math import inf, degrees, atan2, sin, cos, radians
from ray import Ray

YELLOW = (200,200,100)

class Particle:

    def __init__(self, color, display):
        self.pos = math.Vector2(display[0]/3, display[1]/3)
        self.rays = []
        self.color = color
        self.angle = 0

        # Angle between -30 and 30 degrees with 0.1 degree accuracy
        for angle in range(-300, 301, 1):
            self.rays.append(Ray(self.pos, angle/10, YELLOW))


    def show(self, surface):
        for ray in self.rays:
            ray.show(surface)
        draw.circle(surface, self.color, self.pos/4, 6)

    def look(self, surface, walls):
        scene = []
        prev = self.rays[0].pos
        for ray in self.rays:
            ray.rotate(self.angle)

            closest = None
            record = inf
            for wall in walls:
                pt = ray.cast(wall)
                if(pt):
                    d = self.pos.distance_to(pt)
                    d = d * cos(radians(ray.initangle)) 
                    if(d < record):
                        record = d
                        closest = pt
            if closest:
                # Draw ray
                draw.polygon(surface, YELLOW, [prev, closest, self.pos])
                # draw.aaline(surface, YELLOW, self.pos, closest)
                prev = closest
            
            scene.append(record)
            
        return scene

    def update(self, display, dm, da):
        # Rotate
        self.angle = self.angle + da
        
        # Translate
        x = self.pos.x + dm * cos(radians(self.angle))
        y = self.pos.y - dm * sin(radians(self.angle))

        # Check bound
        if (x < 0 or x > display[0]):
            x = x - dm * cos(radians(self.angle))
        if (y < 0 or y > display[1]):
            y = y + dm * sin(radians(self.angle))         

        # Update position
        self.pos.update(x, y)
            
