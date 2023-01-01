import pygame
from pygame.locals import *
import sys, time, math, random

from settings import *

DIM = 16

def checkValid(arr, valid):
    for option in arr[::-1]:
        if(option in valid):
            continue
        else:
            arr.remove(option)


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
    grid = [{"collapse": False, "options": ["BLANK","UP","RIGHT","DOWN","LEFT"], "pos": (x, y)} for y in range(DIM) for x in range(DIM)]

    rules = {
        "BLANK": {
            "UP": ["BLANK","UP"],
            "RIGHT": ["BLANK","RIGHT"],
            "DOWN": ["BLANK","DOWN"],
            "LEFT": ["BLANK","LEFT"]
        },
        "UP": {
            "UP": ["RIGHT","DOWN","LEFT"],
            "RIGHT": ["UP","DOWN","LEFT"],
            "DOWN": ["BLANK","DOWN"],
            "LEFT": ["UP","RIGHT","DOWN"]
        },
        "RIGHT": {
            "UP": ["RIGHT","DOWN","LEFT"],
            "RIGHT": ["UP","DOWN","LEFT"],
            "DOWN": ["UP","RIGHT","LEFT"],
            "LEFT": ["BLANK","LEFT"]
        },
        "DOWN": {
            "UP": ["BLANK","UP"],
            "RIGHT": ["UP","DOWN","LEFT"],
            "DOWN": ["UP","RIGHT","LEFT"],
            "LEFT": ["UP","RIGHT","DOWN"]
        },
        "LEFT": {
            "UP": ["RIGHT","DOWN","LEFT"],
            "RIGHT": ["BLANK","RIGHT"],
            "DOWN": ["UP","RIGHT","LEFT"],
            "LEFT": ["UP","RIGHT","DOWN"]
        }
    }
    # print(grid)

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
        gridUncollapsed = list(filter(lambda cell: cell["collapse"] == False, gridCopy))
        gridFiltered = list(filter(lambda cell: len(cell["options"])==len(gridUncollapsed[0]["options"]), gridUncollapsed))

        if (gridFiltered):
            cell = random.choice(gridFiltered)
            cell["collapse"] = True
            pick = random.choice(cell["options"])
            cell["options"] = [pick]

        # Next tiles
        (ix, iy) = cell["pos"]
        # Look up
        if (iy > 0):
            cell_next = grid[ix + (iy-1) * DIM]["options"]
            valid = rules[cell["options"][0]]["UP"]
            checkValid(cell_next, valid)
        # Look right
        if (ix < DIM-1):
            cell_next = grid[ix+1 + (iy) * DIM]["options"]
            valid = rules[cell["options"][0]]["RIGHT"]
            checkValid(cell_next, valid)
        # Look down
        if (iy < DIM-1):
            cell_next = grid[ix + (iy+1) * DIM]["options"]
            valid = rules[cell["options"][0]]["DOWN"]
            checkValid(cell_next, valid)
        # Look left
        if (ix > 0):
            cell_next = grid[ix-1 + (iy) * DIM]["options"]
            valid = rules[cell["options"][0]]["LEFT"]
            checkValid(cell_next, valid)

        # Draw grid
        for cell in grid:
            (x, y) = tuple([z * 50 for z in cell["pos"]])
            if cell["collapse"]:
                displaysurface.blit(tiles[cell["options"][0]], (x,y))
            else:
                # text = font.render(f'{len(cell["options"])}', True, WHITE)
                # text_rect = text.get_rect(center=(x+25,y+25))
                # displaysurface.blit(text,text_rect)
                pass

        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
