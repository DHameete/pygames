import pygame
from pygame.locals import *
import sys, time, math, random

from settings import *

DIM = 8

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

    #  Load images
    tiles = {
        "BLANK": pygame.image.load("source/blank.png").convert_alpha(),
        "UP": pygame.image.load("source/up.png").convert_alpha(),
        "RIGHT": pygame.image.load("source/right.png").convert_alpha(),
        "DOWN": pygame.image.load("source/down.png").convert_alpha(),
        "LEFT": pygame.image.load("source/left.png").convert_alpha()
    }

    # Create empty grid
    grid = [{"collapse": False, "options": ["BLANK","UP","RIGHT","DOWN", "LEFT"], "index": idx} for idx in range(DIM*DIM)]

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

        # Pick cell with lowest entropy
        gridCopy = grid[:]
        gridCopy.sort(key=lambda cell: len(cell["options"]))
        gridFiltered = list(filter(lambda cell: len(cell["options"])==len(gridCopy[0]["options"]), gridCopy))

        if (gridFiltered):
            cell = random.choice(gridFiltered)
            cell["collapse"] = True
            pick = random.choice(cell["options"])
            cell["options"] = [pick]

        # Draw grid
        for cell in grid:
            if cell["collapse"]:
                idx = cell["index"]
                y = (idx // DIM) * 50
                x = (idx % DIM) * 50
                displaysurface.blit(tiles[cell["options"][0]], (x,y))


        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
