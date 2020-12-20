import pygame
from pygame.locals import *
import sys, time, math

from settings import *
from grid import Grid

def heuristic(a, b):
    # d = math.sqrt( (a.r - b.r)**2 + (a.c - b.c)**2 )
    d = abs(a.r-b.r) + abs(a.c-b.c)
    return d


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


    rows = 25
    cols = 25
    

    # Making 2D-grid
    grid = Grid(cols,rows)
    print(f"rows: {len(grid.spots)}, cols: {len(grid.spots[0])}")

    grid.checkNeighbor()

    openSets = []
    closedSets = []
    
    start = grid.spots[0][0]
    end = grid.spots[-1][-1]

    start.wall = False
    end.wall = False

    openSets.append(start)

    running = True

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
        
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False

            if (len(openSets) > 0):
                current = openSets[0]
            
                for open in openSets:
                    if open.f < current.f:
                        current = open


                if current == end:
                    running = False
                    print("DONE!")

                openSets.remove(current)
                closedSets.append(current)

                neighbors = current.neighbors
                for neighbor in neighbors:
                    if neighbor in closedSets:
                        continue
                    
                    if neighbor.wall:
                        continue

                    tempG = current.g + 1
                    if neighbor in openSets:
                        if tempG < neighbor.g:
                            neighbor.g = tempG
                    else:
                        neighbor.g = tempG
                        openSets.append(neighbor)

                    neighbor.h = heuristic(neighbor,end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = current
            else:
                # no solution
                running = False
                print("No solution")


            # Show grid
            grid.show(displaysurface)

            # Show open and closed sets on grid
            for openSet in openSets:
                openSet.show(displaysurface, GREEN)

            for closedSet in closedSets:
                closedSet.show(displaysurface, RED)
            
            path = []
            temp = current
            path.append(temp)
            while(temp.previous):
                path.append(temp.previous)
                temp = temp.previous
            for p in path:
                p.show(displaysurface,BLUE)

            # Update display
            pygame.display.update()



if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
