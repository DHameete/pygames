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
    points = []
    for _ in range(100):
        point = Point()
        points.append(point)

    # Next index to train perceptron 
    nextind = 0


    training_data = [
        {'input': [0,1], 'target':[1]},
        {'input': [1,0], 'target':[1]},
        {'input': [1,1], 'target':[0]},
        {'input': [0,0], 'target':[0]},
    ]

    nn = NeuralNetwork(2,2,1)

    for _ in range(50000):
        data = random.choice(training_data)
        inputs_nn = Matrix.fromArray(data['input'])
        targets_nn = Matrix.fromArray(data['target'])

        nn.train(inputs_nn, targets_nn)

    for data in training_data:
        inputs_nn = Matrix.fromArray(data['input'])
        (outputs_nn, _) = nn.feedforward(inputs_nn)
        print(f"in: {inputs_nn} out: {outputs_nn}")


    # loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

        # Background surface
        displaysurface.fill(DARKGRAY)

        # Show points
        for point in points:
            guess = p.guess(point)
            if guess == point.label:
                point.show(displaysurface, GREEN)
            else:
                point.show(displaysurface, ORANGE)

        # Train per point
        nextpoint = points[nextind]
        p.train(nextpoint)

        # Show perceptrion
        p.show(displaysurface)

        # Update and show text
        w = [round(pw, 2) for pw in p.weights]
        text4 = font.render(f'{w}', True, WHITE)
        text_rect4 = text4.get_rect(center=(75,25))
        displaysurface.blit(text4,text_rect4)

        # Increment index
        nextind = (nextind + 1) % len(points)

        # Update display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
