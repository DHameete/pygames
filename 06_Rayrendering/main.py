import pygame
from pygame.locals import *
import sys, random, math
from noise import pnoise1

from wall import Wall
from particle import Particle

width = 800
height = 600

WHITE = (255, 255, 255)
YELLOW = (200, 200, 100)
BLUE = (0, 50, 200)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
GRAY = (51, 51, 51)

def main():

    # setup
    pygame.init()
    display = (width, height)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Rayrendering")

    # Initialize boundaries
    walls = []
    walls.append(Wall((-1,-1),(width,-1),WHITE))
    walls.append(Wall((width,-1),(width,height),WHITE))
    walls.append(Wall((width,height),(-1,height),WHITE))
    walls.append(Wall((-1,height),(-1,-1),WHITE))

    # Initialize walls
    for _ in range(8):
        p1 = (random.randrange(width),random.randrange(height))
        p2 = (random.randrange(width),random.randrange(height))
        walls.append(Wall(p1,p2,WHITE))

    # Initialize particle
    particle = Particle(WHITE,display)

    # Initialize movement variables
    move = 0
    rotate = 0
    direction_speed = 3
    rotation_speed = 3
    buttons_pressed = 0

    # Initialize noise variables
    m_off = 0
    a_off = 0
    m_amp = random.randint(2,6)
    a_amp = random.randint(2,6)
    dm = random.randint(5,15)/1000
    da = random.randint(5,15)/1000

    # projection plane is required for fisheye fix
    distProjPlane = (width / 50) / math.tan(math.radians(60) / 2)

    # draw-loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Move by keyboard
            if event.type == KEYDOWN:
                if event.key in {K_UP, K_w}:
                    move = direction_speed
                    buttons_pressed += 1
                if event.key in {K_DOWN, K_s}:
                    move = -direction_speed
                    buttons_pressed += 1
                if event.key in {K_LEFT, K_a}:
                    rotate = rotation_speed
                    buttons_pressed += 1
                if event.key in {K_RIGHT, K_d}:
                    rotate = -rotation_speed
                    buttons_pressed += 1
            # Stop moving when unpressed
            if event.type == KEYUP:
                if event.key in {K_UP, K_w, K_DOWN, K_s}:
                    move = 0
                    buttons_pressed -= 1
                if event.key in {K_LEFT, K_a, K_RIGHT, K_d}:
                    rotate = 0
                    buttons_pressed -= 1
        
        # Perlin noise
        if(not buttons_pressed):
            m_off += dm
            a_off += da
            move = pnoise1(m_off, 1) * m_amp
            rotate = pnoise1(a_off, 1) * a_amp

        # Draw background
        displaysurface.fill(GRAY)
        
        # Set particle position
        particle.update(display, move, rotate)

        # Calculate distance to walls
        scene = particle.look(displaysurface, walls)

        # Draw grass and air
        pygame.draw.rect(displaysurface,BLUE,(0,0,width,height/2))
        pygame.draw.rect(displaysurface,GREEN,(0,height/2,width,height/2))

        # Ray rendering
        w = (width / len(scene))
        for ind, line in enumerate(scene):
            line = max(min(line,width), 0)
            clr = math.floor((205/(width*width))*(line-width)*(line-width) + 50) # y = a * (x-h)^2 + k

            line_min = max(line,30)
            h = (width / line_min) * distProjPlane
            
            pygame.draw.rect(displaysurface, (clr,clr,clr), (ind * w, (height-h)/2, w, h), 3)

        # Draw map background
        pygame.draw.rect(displaysurface, GRAY, (0, 0, width/4, height/4))
        
        # Draw particle and rays
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