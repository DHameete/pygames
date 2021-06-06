import pygame
from pygame.locals import *
import pygame.freetype
import sys, time, math, random, os

from settings import *
from nn import NeuralNetwork

from matrix import Matrix
from matmath import MatMath

import numpy as np


def splitData(name):
    filename = f'data/{name}400.bin'
    with open(filename, mode='rb') as file: # b is important -> binary
        data = file.read()

    output = {
        "training": {
            "data": [],
            "label": []
        },
        "testing": {
            "data": [],
            "label": []
        }
    }
    
    for i in range(TOTAL_DATA):
        if i < math.floor(TOTAL_DATA*0.8):
            output["training"]["data"].append(data[i*SIZE:i*SIZE+SIZE])
            output["training"]["label"] = labels[name]
        else:
            output["testing"]["data"].append(data[i*SIZE:i*SIZE+SIZE])
            output["testing"]["label"] = labels[name]
    return output

def main():

    # setup
    pygame.init()
    display = (WIDTH, HEIGHT)
    displaysurface = pygame.display.set_mode(display)
    anglcolorpalette=[(255-x,255-x,255-x) for x in range(0,256)]

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
    text_black_rect.center = (WIDTH/4, HEIGHT/2)

    airplanes = splitData('airplane')
    cars = splitData('car')
    trucks = splitData('truck')
    
    ind_pick = random.randrange(len(airplanes["training"]["data"]))
    img_surf = pygame.image.frombuffer(airplanes["training"]["data"][ind_pick],(28,28),"P")
    img_surf.set_palette(anglcolorpalette)
    print(airplanes["training"]["label"])

    # New neural network
    nn = NeuralNetwork(784, 64, 3)

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

        # Background surface
        displaysurface.fill(DARKGRAY)

        # Draw text
        # ft_font.render_to(displaysurface, text_black_rect.topleft, text_black, BLACK)

        pygame.Surface.blit(displaysurface,img_surf, (0,0))

        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
