import pygame
import random, math

from settings import *

def activate(sum_input):
    return (1 if sum_input >= 0 else -1)

class Perceptron:

    def __init__(self, num):

        # Learning rate
        self.lr = 0.1

        # Initialize weights randomly
        self.weights = []
        for n in range(num):
            w = random.uniform(-1, 1)
            self.weights.append(w)

        self.pos1 = pygame.Vector2(0,0)
        self.pos2 = pygame.Vector2(WIDTH,0)

    
    def guess(self, inputs):
        weighted_sum = 0

        # Calculate weighted sum
        for ind, weight in enumerate(self.weights):
            weighted_sum += weight * inputs[ind]

        # Evaluate activation function
        output = activate(weighted_sum)
        return output

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess

        # Tune weights
        for ind, weight in enumerate(self.weights):
            self.weights[ind] += error * inputs[ind] * self.lr

    def show(self, surface):
        x1 = 0
        x2 = WIDTH 
        
        y1 = -self.weights[0] / self.weights[1] * x1
        y2 = -self.weights[0] / self.weights[1] * x2

        self.pos1 = self.pos1.lerp(pygame.Vector2(x1,y1),0.1)
        self.pos2 = self.pos2.lerp(pygame.Vector2(x2,y2),0.1)

        pygame.draw.line(surface, WHITE, self.pos1, self.pos2, 2)

