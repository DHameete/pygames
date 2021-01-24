import pygame
from pygame.locals import *
import sys, time, math, random

from settings import *
from firework import Firework

def main():

    # setup
    pygame.init()
    display = (WIDTH, HEIGHT)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Fireworks")

    clock = pygame.time.Clock()

    # Draw background
    displaysurface.fill(DARKGRAY)
    pygame.display.update()

    # Font
    font = pygame.font.SysFont('Arial', 36)
    font.set_bold(True)

    N = 10
    
    fireworks = []
    fireworks.append(Firework())
    gravity = pygame.math.Vector2(0, 0.2)


    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

        displaysurface.fill(DARKGRAY)

        if random.random() < 0.05:
            fireworks.append(Firework())

        for firework in fireworks:
            firework.update(gravity)
            firework.show(displaysurface)

        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
