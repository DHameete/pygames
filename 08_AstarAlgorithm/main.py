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

    # setup
    pygame.init()
    display = (WIDTH, HEIGHT)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("A* algorithm")

    clock = pygame.time.Clock()

    # Draw background
    displaysurface.fill((51, 51, 51))
    pygame.display.update()

    # Amount of rows and cols
    rows = 50
    cols = 50
    
    # Font
    font = pygame.font.SysFont('Arial', 36)
    font.set_bold(True)

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
    best = start

    # Restart
    rect1 = pygame.Rect(WIDTH/2-10,HEIGHT/2-30,20,20)
    text1 = ''
    
    rect2 = pygame.Rect(WIDTH/2-10,HEIGHT/2+10,20,20)
    text2img = font.render('Restart? Press R.', True, ORANGE)
    text_rect2 = text2img.get_rect(center=rect2.center)

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

            if event.type == KEYDOWN:
                if event.key == K_r:
                    # Draw background
                    displaysurface.fill((51, 51, 51))

                    grid = Grid(cols,rows)
                    grid.checkNeighbor()
                    
                    openSets = []
                    closedSets = []

                    start = grid.spots[0][0]
                    end = grid.spots[-1][-1]

                    start.wall = False
                    end.wall = False

                    openSets.append(start)

                    running = True
                    best = start

        
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
                    text1 = "Done!"

                openSets.remove(current)
                closedSets.append(current)

                neighbors = current.neighbors
                for neighbor in neighbors:
                    if neighbor in closedSets:
                        continue
                    
                    if neighbor.wall:
                        continue

                    # tempG = current.g + 1
                    tempG = current.g + heuristic(current,neighbor)
                    newPath = False
                    if neighbor in openSets:
                        if tempG < neighbor.g:
                            neighbor.g = tempG
                            newPath = True
                    else:
                        neighbor.g = tempG
                        newPath = True
                        openSets.append(neighbor)

                    if newPath:
                        neighbor.h = heuristic(neighbor,end)
                        neighbor.f = neighbor.g + neighbor.h
                        neighbor.previous = current

                        if neighbor.h < best.h:
                            best = neighbor

            else:
                # no solution
                current = best
                running = False
                text1 = 'No solution..'

            displaysurface.fill((51, 51, 51))

            # Show grid
            grid.show(displaysurface)

            # Show open and closed sets on grid
            for openSet in openSets:
                openSet.show(displaysurface, OPEN_COLOR)

            for closedSet in closedSets:
                closedSet.show(displaysurface, CLOSED_COLOR)
            
            start.show(displaysurface,BEST_COLOR)
            end.show(displaysurface, ORANGE)

            path = []
            temp = current
            path.append(temp)
            points = []
            while(temp.previous):
                path.append(temp.previous)
                temp = temp.previous
            for p in path:
                # p.show(displaysurface,BLUE)
                points.append([p.c*p.width + p.width/2-1, p.r*p.height + p.height/2-1])
            
            path = []
            temp = best
            path.append(temp)
            pointsBest = []
            while(temp.previous):
                path.append(temp.previous)
                temp = temp.previous
            for p in path:
                # p.show(displaysurface,BLUE)
                pointsBest.append([p.c*p.width + p.width/2-1, p.r*p.height + p.height/2-1])

            if len(points)>1:
                pygame.draw.lines(displaysurface,BEST_COLOR,False,points,4)
                pygame.draw.lines(displaysurface,ORANGE,False,pointsBest,4)

            if not running:
                text1img = font.render(text1, True, ORANGE)
                text_rect1 = text1img.get_rect(center=rect1.center)
                displaysurface.blit(text1img, text_rect1)
                displaysurface.blit(text2img, text_rect2)

            # Update display
            pygame.display.update()
            clock.tick(60)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
