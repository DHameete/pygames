import pygame


class Particle:

    def __init__(self, pos, vel, color):
        self.pos = pygame.math.Vector2(pos)
        self.vel = pygame.math.Vector2(0,vel)
        self.acc = pygame.math.Vector2(0,0)

        self.color = color

    def applyForce(self, force):
        self.acc += force

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc.update(0)

    def show(self, surface):
        pygame.draw.circle(surface, (255,255,255), self.pos, 3)