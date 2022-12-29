import pygame
from pygame.locals import *
import sys, time, math, random

from settings import *

def main():

    # setup
    pygame.init()
    display = (WIDTH, HEIGHT)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Wave Function Collapse")

    # Draw background
    displaysurface.fill(DARKGRAY)
    pygame.display.update()

    # Clock
    clock = pygame.time.Clock()

    # Font
    font = pygame.font.SysFont('Arial', 36)
    font.set_bold(True)

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

        # Background surface
        background_surface = pygame.Surface((WIDTH,HEIGHT))
        background_surface.set_alpha(100) 
        background_surface.fill(DARKGRAY)
        displaysurface.blit(background_surface, (0,0))


        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
