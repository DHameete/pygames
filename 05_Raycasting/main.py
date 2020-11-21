import pygame
from pygame.locals import QUIT
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
    particle = Particle(WHITE)

    # draw-loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Draw background
        displaysurface.fill((51, 51, 51))
        
        # Set particle position
        mouse = pygame.mouse.get_pos()
        particle.update(width/3, height/6, mouse)
        
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