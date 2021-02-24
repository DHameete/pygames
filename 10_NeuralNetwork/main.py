import pygame
from pygame.locals import *
import sys, time, math, random

from settings import *
from perceptron import Perceptron
from point import Point
from nn import NeuralNetwork

from matrix import Matrix
from matmath import MatMath

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
    font = pygame.font.SysFont('Arial', 16)
    font.set_bold(True)

    # Text
    text4 = font.render(f'{0}', True, WHITE)
    text_rect4 = text4.get_rect(center=(20,25))

    # Initialize perceptrion
    p = Perceptron(2)

    # Initialize inputs
    training_data = []
    for _ in range(500):
        point = Point()
        training_data.append(point)

    test_data = []
    for _ in range(100):
        point = Point()
        test_data.append(point)

    # Next index to train perceptron 
    nextind = 0

    nn = NeuralNetwork(2,2,1)

    for data in training_data:
        nn.train([data.x,data.y], [data.label])

    # Show points
    for point in test_data:
        guess = nn.guess([point.x,point.y])

        print(f"guess: {guess}, label: {point.label}")
        v = min(abs(guess[0] - point.label),1)


    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

        # Background surface
        displaysurface.fill(DARKGRAY)

        # Show points
        for point in test_data:
            # guess = p.guess(point)
            guess = nn.guess([point.x,point.y])

            v = min(abs(guess[0] - point.label),1)
            c = GREEN.lerp(RED, v)

            point.show(displaysurface, c)


        # Train per point
        for _ in range(10):
            nextpoint = random.choice(training_data)
            nn.train([nextpoint.x,nextpoint.y], [nextpoint.label])
            guess = nn.guess([nextpoint.x,nextpoint.y])

        # Update and show text
        w = [round(pw, 2) for pw in p.weights]
        text4 = font.render(f'{w}', True, WHITE)
        text_rect4 = text4.get_rect(center=(75,25))
        displaysurface.blit(text4,text_rect4)

        # Increment index
        nextind = (nextind + 1) % len(training_data)

        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
