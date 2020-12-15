import pygame
from pygame.locals import *
import sys, time, math


width = 800
height = 600

WHITE = (255, 255, 255)


def main():

    # setup
    pygame.init()
    display = (width, height)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("A* algorithm")

    # Draw background
    displaysurface.fill((51, 51, 51))

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

        # Update display
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
