import pygame, math

from settings import *
from matrix import Matrix
from matmath import MatMath

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def dsigmoid(y):
    # y is already the sigmoid input
    return y * (1 - y)


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
        hidden_nn = MatMath.multiply(self.weights_ih,input_nn)
        hidden_nn.add(self.bias_h)

        # Activation function on hidden
        hidden_nn.map(sigmoid)

        # Generate output
        output_nn = MatMath.multiply(self.weights_ho,hidden_nn)
        output_nn.add(self.bias_o)

        # Activation function on output
        output_nn.map(sigmoid)

        return output_nn

    
    def train(self, input_nn, targets):
        output_nn = self.feedforward(input_nn)

        # Calculate the output error
        # ERROR = TARGETS - OUTPUTS
        output_errors = MatMath.subtract(targets, output_nn)
        output_nn.map(dsigmoid)


        # Calculate the hidden layer errors
        weights_ho_T = MatMath.transpose(self.weights_ho)
        hidden_errors = MatMath.multiply(weights_ho_T,output_errors)

        print(hidden_errors)