import pygame
from pygame.locals import *
import sys, time, math, random

from settings import *
from perceptron import Perceptron
from point import Point

def main():

    # setup
    pygame.init()
    display = (WIDTH, HEIGHT)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Neural Network!")

    # Draw background
    displaysurface.fill(DARKGRAY)
    pygame.display.update()

    # Clock
    clock = pygame.time.Clock()

    # Font
    font = pygame.font.SysFont('Arial', 36)
    font.set_bold(True)

    p = Perceptron(2)

    points = []
    for _ in range(100):
        point = Point()
        points.append(point)

    nextind = 0

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

        # Background surface
        displaysurface.fill(DARKGRAY)

        for point in points:
            guess = p.guess((point.x, point.y))
            if guess == point.label:
                point.show(displaysurface, GREEN)
            else:
                point.show(displaysurface, ORANGE)

        # Train per point
        nextpoint = points[nextind]
        p.train((nextpoint.x, nextpoint.y), nextpoint.label)
        p.show(displaysurface)
        nextind += 1
        nextind %= len(points)

        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
