import pygame


class Particle:

    def __init__(self, pos, vel, color):
        self.pos = pygame.math.Vector2(pos)
        self.vel = pygame.math.Vector2(vel)
        self.acc = pygame.math.Vector2(0,0)

        self.color = color

    def applyForce(self, force):
        self.acc += force

    def update(self):
        self.vel += self.acc
        self.vel *= 0.95 # drag
        self.pos += self.vel
        self.acc.update(0)

    def show(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, 3)