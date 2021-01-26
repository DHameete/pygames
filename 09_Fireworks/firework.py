import pygame, random, colorsys
from settings import *

from particle import Particle


class Firework():

    def __init__(self):
        pos = (random.randrange(WIDTH),HEIGHT)
        vel = (0,-1*random.randrange(15,25))

        color_normal = colorsys.hsv_to_rgb(random.random(),0.4,1)
        self.color = tuple([255*c for c in color_normal])
        self.seed = Particle(pos,vel,self.color)
        
        self.particles = []
        self.exploded = False

        self.lifespan = 255

    def update(self, force): 
        if not self.exploded:
            self.seed.applyForce(force)
            self.seed.update()

            if self.seed.vel.y >= 0:
                self.exploded = True
                self.explode()
        
        else:
            self.lifespan -= 8
            for p in self.particles:
                p.applyForce(force)
                p.update()

    def explode(self):
        for i in range(100):
            vel = pygame.math.Vector2()
            
            # r = random.uniform(1, 6)
            r = random.uniform(4, 10)
            phi = random.randrange(361)
            vel.from_polar((r, phi))

            self.particles.append(Particle(self.seed.pos, vel, self.color))


    def show(self,surface):
        if not self.exploded:
            self.seed.show(surface)
        else:
            # temporary surface
            surface2 = pygame.Surface((WIDTH,HEIGHT))
            surface2.set_colorkey((0,0,0))
            surface2.set_alpha(self.lifespan) 

            for p in self.particles:
                p.show(surface2)

            surface.blit(surface2, (0,0))
