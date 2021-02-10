import pygame
import random, math

from settings import *

def activate(sum_input):
    return (1 if sum_input >= 0 else -1)

class Perceptron:

    def __init__(self, num):

        # Learning rate
        self.lr = 0.6

        # Initialize weights randomly
        self.weights = []
        for n in range(num):
            w = random.uniform(-1, 1)
            self.weights.append(w)

        self.pos1 = pygame.Vector2(0,0)
        self.pos2 = pygame.Vector2(WIDTH,0)

    
    def guess(self, point):
        weighted_sum = 0

        # Calculate weighted sum
        inputs = (point.x, point.y)
        for ind, weight in enumerate(self.weights):
            weighted_sum += weight * inputs[ind]
        weighted_sum += point.bias

        # Evaluate activation function
        output = activate(weighted_sum)
        return output

    def train(self, point):
        
        guess = self.guess(point)
        target = point.label

        error = target - guess

        inputs = (point.x, point.y)

        # Tune weights
        for ind, weight in enumerate(self.weights):
            self.weights[ind] += error * inputs[ind] * self.lr 
    
    def pixels(self, x, y):
        return ((1 + x) / 2 * WIDTH, (1 - y) / 2 * HEIGHT)
    
    def show(self, surface):
        x1 = -1
        x2 = 1 
        bias = 1
        
        y1 = -self.weights[0] / self.weights[1] * x1 - bias / self.weights[1]
        y2 = -self.weights[0] / self.weights[1] * x2 - bias / self.weights[1]

        self.pos1 = self.pos1.lerp(pygame.Vector2(self.pixels(x1,y1)),0.1)
        self.pos2 = self.pos2.lerp(pygame.Vector2(self.pixels(x2,y2)),0.1)

        pygame.draw.line(surface, WHITE, self.pos1, self.pos2, 2)

