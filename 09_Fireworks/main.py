import pygame
from pygame.locals import *
import sys, time, math, random

from settings import *
from firework import Firework

def main():

    # setup
    pygame.init()
    display = (WIDTH, HEIGHT)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Fireworks")

    # Draw background
    displaysurface.fill(DARKGRAY)
    pygame.display.update()

    # Clock
    clock = pygame.time.Clock()

    # Font
    font = pygame.font.SysFont('Arial', 36)
    font.set_bold(True)

    # Firework
    fireworks = []
    fireworks.append(Firework())
    gravity = pygame.math.Vector2(0, 0.2)

    # Text
    text4 = font.render(f'{0}', True, WHITE)
    text_rect4 = text4.get_rect(center=(20,25))

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

        # Create firework
        if random.random() < 0.05:
            fireworks.append(Firework())

        # Update and show firework
        for firework in fireworks[:]:
            firework.update(gravity)
            firework.show(displaysurface)
            
            if firework.lifespan < 0:
                fireworks.remove(firework)

        # Update and show text
        text4 = font.render(f'{len(fireworks)}', True, WHITE)
        text_rect4 = text4.get_rect(center=(20,25))
        displaysurface.blit(text4,text_rect4)

        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
