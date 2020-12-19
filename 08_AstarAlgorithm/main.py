import pygame
from pygame.locals import *
import sys, time, math

from settings import *
from grid import Grid



def main():

    # Init globals
    # settings.init()

    # setup
    pygame.init()
    display = (WIDTH, HEIGHT)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("A* algorithm")

    # Draw background
    displaysurface.fill((51, 51, 51))


    rows = 5
    cols = 6
    

    # Making 2D-grid
    grid = Grid(cols,rows)
    print(f"rows: {len(grid.spots)}, cols: {len(grid.spots[0])}")

    grid.checkNeighbor()

    openSets = []
    closedSets = []

    start = grid.spots[0][0]
    end = grid.spots[-1][-1]

    openSets.append(start)

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
        
        if (len(openSets) > 0):
            current = openSets[0]
        
            for open in openSets:
                if open.f < current.f:
                    current = open


            if current == end:
                print("DONE!")

            openSets.remove(current)
            closedSets.append(current)

            neighbors = current.neighbors
            print(neighbors)

        else:
            # no solution
            pass
            # print("ELSE")

        # Show grid
        grid.show(displaysurface)

        # Show open and closed sets on grid
        for openSet in openSets:
            openSet.show(displaysurface, GREEN)

        for closedSet in closedSets:
            closedSet.show(displaysurface, RED)

        # Update display
        pygame.display.update()



if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
