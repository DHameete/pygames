import pygame
from pygame.locals import *
import pygame.freetype
import sys, time, math, random

from settings import *
from nn import NeuralNetwork

from matrix import Matrix
from matmath import MatMath


def pickColor():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)

    color = pygame.Color(r, g, b)
    return color

def colorPredictor(inputs, brain):
    
    outputs = brain.guess(inputs)
    print(outputs)

    if outputs[0] > outputs[1]:
        return "Black"
    else:
        return "White"


def trainColor(color):
    if sum(color[:-1]) > 400:
        return [1, 0] # Black
    else:
        return [0, 1] # White

def main():

    # setup
    pygame.init()
    display = (WIDTH, HEIGHT)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Color Predictor!")

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

    text_white = 'White'
    text_white_rect = ft_font.get_rect(text_white)
    text_white_rect.center = (3*WIDTH/4,HEIGHT/2)

    # New neural network
    brain = NeuralNetwork(3,3,2)

    # Train
    for _ in range(1000):
        color = pickColor()
        
        inputs = [element/255 for element in color[:-1]]
        targets = trainColor(color)
        
        brain.train(inputs,targets)

    # Colors
    color = pickColor()
    
    inputs = [element/255 for element in color[:-1]]
    choice = colorPredictor(inputs, brain)
    

    circle_black = pygame.Rect(0,0,30,30)
    circle_black.center = (WIDTH/4, 3*HEIGHT/4)
    circle_white = circle_black.copy()
    circle_white.center = (3*WIDTH/4, 3*HEIGHT/4)

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:

                mouse = pygame.mouse.get_pos()
                if mouse[0] > WIDTH/2:
                    targets = [0, 1]
                else:
                    targets = [1, 0]

                # Train network
                brain.train(inputs,targets)

                # New color
                color = pickColor()
                
                print(color[:-1], sum(color[:-1]))
                
                inputs = [element/255 for element in color[:-1]]
                choice = colorPredictor(inputs, brain)


        # Background surface
        displaysurface.fill(color)

        # Draw mid-line
        pygame.draw.line(displaysurface,BLACK,(WIDTH/2,0),(WIDTH/2,HEIGHT))


        if choice == "Black":
            pygame.draw.ellipse(displaysurface, BLACK, circle_black)
        else:
            pygame.draw.ellipse(displaysurface, WHITE, circle_white)

        # Draw text
        ft_font.render_to(displaysurface, text_black_rect.topleft, text_black, BLACK)
        ft_font.render_to(displaysurface, text_white_rect.topleft, text_white, WHITE)

        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
