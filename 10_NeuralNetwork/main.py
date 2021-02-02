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

    # Initialize perceptrion
    p = Perceptron(3)

    # Initialize inputs
    points = []
    for _ in range(100):
        point = Point()
        points.append(point)

    # Next index to train perceptron 
    nextind = 0

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

        # Background surface
        displaysurface.fill(DARKGRAY)

        # Show points
        for point in points:
            guess = p.guess((point.x, point.y, point.bias))
            if guess == point.label:
                point.show(displaysurface, GREEN)
            else:
                point.show(displaysurface, ORANGE)

        # Train per point
        nextpoint = points[nextind]
        p.train((nextpoint.x, nextpoint.y, nextpoint.bias), nextpoint.label)

        # Show perceptrion
        p.show(displaysurface)

        # Increment index
        nextind = (nextind + 1) % len(points)

        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
