import pygame, random
from settings import *

from particle import Particle


class Firework():

    def __init__(self):
        vel = -1*random.randrange(8,13)
        self.p = Particle((random.randrange(WIDTH),HEIGHT),vel,WHITE)

    def update(self, force):
        self.p.applyForce(force)
        self.p.update()

    def show(self,surface):
        self.p.show(surface)