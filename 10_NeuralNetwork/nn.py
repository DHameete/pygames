import pygame, math

from settings import *
from matrix import Matrix

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

class NeuralNetwork:

    def __init__(self, numI, numH, numO):
        self.input_nodes = numI
        self.hidden_nodes = numH
        self.output_nodes = numO

        self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = Matrix(self.hidden_nodes, 1)
        self.bias_o = Matrix(self.output_nodes, 1)
        self.bias_h.randomize()
        self.bias_o.randomize()

    def feedforward(self, input_nn):

        # Generate hidden output
        hidden_nn = self.weights_ih.multiply(input_nn)
        hidden_nn.add(self.bias_h)

        # Activation function
        hidden_nn.map(sigmoid)

        output_nn = self.weights_ho.multiply(hidden_nn)
        output_nn.add(self.bias_o)
        output_nn.map(sigmoid)

        return output_nn