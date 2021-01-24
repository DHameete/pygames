import pygame, random
from settings import *

from particle import Particle


class Firework():

    def __init__(self):
        pos = (random.randrange(WIDTH),HEIGHT)
        vel = (0,-1*random.randrange(15,25))
        # vel = (0,-1*10)
        self.seed = Particle(pos,vel,WHITE)
        
        self.particles = []
        self.exploded = False

    def update(self, force): 
        if not self.exploded:
            self.seed.applyForce(force)
            self.seed.update()

            if self.seed.vel.y >= 0:
                self.exploded = True
                self.explode()
        else:
            for p in self.particles:
                p.applyForce(force)
                p.update()

    def explode(self):
        for i in range(100):
            vel = pygame.math.Vector2()
            
            r = random.uniform(1, 6)
            phi = random.randrange(361)
            vel.from_polar((r, phi))

            self.particles.append(Particle(self.seed.pos, vel, WHITE))


    def show(self,surface):
        if not self.exploded:
            self.seed.show(surface)
        else:
            for p in self.particles:
                p.show(surface)