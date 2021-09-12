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
        "training": [],
        "testing": []
    }
    
    data_arr = {
        "data": [],
        "label": []
    }
    
    for i in range(TOTAL_DATA):
        data_arr["data"] = data[i*SIZE:i*SIZE+SIZE]
        data_arr["label"] = labels[name]
        if i < math.floor(TOTAL_DATA*0.8):
            output["training"].append(data_arr)
        else:
            output["testing"].append(data_arr)
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

    # Extra data
    airplanes = splitData('airplane')
    cars = splitData('car')
    trucks = splitData('truck')

    # Prepare training data
    training = []
    training += airplanes["training"]
    training += cars["training"]
    training += trucks["training"]
    random.shuffle(training)

    ind_pick = random.randrange(len(training))
    img_surf = pygame.image.frombuffer(training[0]["data"],(28,28),"P")
    img_surf.set_palette(anglcolorpalette)
    
    # New neural network
    nn = NeuralNetwork(784, 64, 3)

    # Train
    for ndx in range(0,len(training)):
        inputs = [data / 255.0 for data in training[ndx]["data"]]
        targets = [0, 0, 0]
        targets[training[ndx]["label"]] = 1

        nn.train(inputs,targets)

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
