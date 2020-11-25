import pygame
from pygame.locals import *
import sys
import random


width = 800
height = 600

WHITE = (255, 255, 255)
BLUE = (0, 255, 255)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)

def main():

    # setup
    pygame.init()
    display = (width, height)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Chaos game")

    points = []
    for _ in range(3):
        x = random.randint(0, width)
        y = random.randint(0, height)
        points.append(pygame.Vector2(x,y))
    diff_vec = points[1] - points[0]
    diff_vec.rotate_ip(60)
    points[2] = points[0] + diff_vec
    if points[2].x < 0 or points[2].x > width or points[2].y < 0 or points[2].y > height:
        diff_vec.rotate_ip(-120)
        points[2] = points[0] + diff_vec


    x_pos = random.randint(0, width)
    y_pos = random.randint(0, height)
    pos = pygame.Vector2(x_pos, y_pos)
    
    clr = BLUE

    displaysurface.fill((51, 51, 51))

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Draw background

        # Draw points
        for point in points:
            pygame.draw.circle(displaysurface, WHITE, point, 3)

        # pygame.draw.circle(displaysurface, BLUE, pos, 2)

        # Update display
        pygame.display.update()

        for _ in range(10):
            r = random.randint(0,3)

            if r == 0:
                pos = pos.lerp(points[0],0.5)
                clr = BLUE
            elif r == 1:
                pos = pos.lerp(points[1],0.5)
                clr = YELLOW
            else:
                pos = pos.lerp(points[2],0.5)
                clr = ORANGE
            pygame.draw.circle(displaysurface, clr, pos, 2)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
