import pygame
from pygame.locals import *
import sys, random, math

from wall import Wall
from particle import Particle

width = 800
height = 600

WHITE = (255, 255, 255)
YELLOW = (200,200,100)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

def main():

    # setup
    pygame.init()
    display = (width, height)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Raycasting")

    # Initialize boundaries
    walls = []
    walls.append(Wall((-1,-1),(width,-1),BLUE))
    walls.append(Wall((width,-1),(width,height),BLUE))
    walls.append(Wall((width,height),(-1,height),BLUE))
    walls.append(Wall((-1,height),(-1,-1),BLUE))

    # Initialize walls
    for _ in range(5):
        p1 = (random.randrange(width),random.randrange(height))
        p2 = (random.randrange(width),random.randrange(height))
        walls.append(Wall(p1,p2,BLUE))

    # Initialize particle
    particle = Particle(WHITE,display)

    x_move = 0
    y_move = 0
    direction_speed = 3

    # draw-loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key in {K_LEFT, K_a}:
                    x_move = -direction_speed
                if event.key in {K_RIGHT, K_d}:
                    x_move = direction_speed
                if event.key in {K_UP, K_w}:
                    y_move = -direction_speed
                if event.key in {K_DOWN, K_s}:
                    y_move = direction_speed

            if event.type == KEYUP:
                if event.key in {K_LEFT, K_a, K_RIGHT, K_d}:
                    x_move = 0
                if event.key in {K_UP, K_w, K_DOWN, K_s}:
                    y_move = 0


        # Draw background
        displaysurface.fill((51, 51, 51))
        
        # Set particle position
        mouse = pygame.mouse.get_pos()
        particle.update(display, x_move, y_move, mouse)

        # Draw particle and rays
        particle.look(displaysurface, walls)
        particle.show(displaysurface)

        # Draw walls
        for wall in walls:
            wall.show(displaysurface)

        # Update display
        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()