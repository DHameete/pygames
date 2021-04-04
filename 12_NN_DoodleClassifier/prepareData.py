import pygame
from pygame.locals import *
import pygame.freetype
import sys, time, math, random, os
import requests, io

from settings import *
from nn import NeuralNetwork

from matrix import Matrix
from matmath import MatMath

import numpy as np


def displaytext(ft_font,displaysurface,text):
    text_black = text
    text_black_rect = ft_font.get_rect(text_black)
    text_black_rect.center = (WIDTH/2,HEIGHT/2)
    
    ft_font.render_to(displaysurface, text_black_rect.topleft, text_black, ORANGE)
    pygame.display.update()


def main():

    # setup
    pygame.init()
    display = (WIDTH, HEIGHT)
    displaysurface = pygame.display.set_mode(display)
    pygame.display.set_caption("Doodle Classifier!")

    # Draw background
    displaysurface.fill(WHITE)
    pygame.display.update()

    # Clock
    clock = pygame.time.Clock()

    # Font
    ft_font = pygame.freetype.SysFont('Arial', 64, True)

    # Select data
    name = "speedboat"

    # Texts
    displaytext(ft_font,displaysurface,f'Loading data...')
    
    # Load data
    lnk = f'https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/{name}.npy'
    response = requests.get(lnk)
    response.raise_for_status()
    indata = np.load(io.BytesIO(response.content))
  
    
    s = 28
    num_indata = indata.shape[0]

    p_size = 1
    rows = math.floor((WIDTH / s) / p_size)

    data_array = []
    outdata = bytearray()
    for _ in range(rows*rows):
        n = random.randrange(num_indata)
        data = indata[n]
        outdata.extend(bytearray(data))
        data_array.append(data)
    
    displaysurface.fill(WHITE)
    displaytext(ft_font,displaysurface,f'Writing data...')
    with open(f'data/{name}400.bin', 'wb') as f:
        f.write(outdata)

    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

        # Background surface
        displaysurface.fill(WHITE)

        # Draw 
        for ind in range(len(data_array)):
            start_x = ind % rows
            start_y = math.floor(ind / rows)

            for y in range(s):
                for x in range(s):
                    c = [255-data_array[ind][s * y + x] for _ in range(3)]
                    pos = ((start_x * s + x) * p_size, (start_y * s + y) * p_size, p_size, p_size)
                    pygame.draw.rect(displaysurface, c, pos)

        # Draw text
        displaytext(ft_font,displaysurface,f'{name}!')

        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
