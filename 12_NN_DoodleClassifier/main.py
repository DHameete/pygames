import pygame
from pygame.locals import *
import pygame.freetype
import sys, time, math, random

from settings import *
from nn import NeuralNetwork

from matrix import Matrix
from matmath import MatMath


def main():

    # setup
    pygame.init()
    display = (WIDTH, HEIGHT)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Doodle Classifier!")

    # Draw background
    displaysurface.fill(DARKGRAY)
    pygame.display.update()

    # Clock
    clock = pygame.time.Clock()

    # Font
    ft_font = pygame.freetype.SysFont('Arial', 64, True)

    # Texts
    text_black = 'Black'
    text_black_rect = ft_font.get_rect(text_black)
    text_black_rect.center = (WIDTH/4,HEIGHT/2)

    # New neural network
    brain = NeuralNetwork(3,3,2)


    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

        # Background surface
        displaysurface.fill(DARKGRAY)

        # Draw text
        ft_font.render_to(displaysurface, text_black_rect.topleft, text_black, BLACK)

        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
