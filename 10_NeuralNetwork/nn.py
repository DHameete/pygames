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
        self.learning_rate = 0.1

    def feedforward(self, inputs):

        # Generate hidden output
        hiddens = MatMath.multiply(self.weights_ih,inputs)
        hiddens.add(self.bias_h)

        # Activation function on hidden
        hiddens.map(sigmoid)

        # Generate output
        outputs = MatMath.multiply(self.weights_ho,hiddens)
        outputs.add(self.bias_o)

        # Activation function on output
        outputs.map(sigmoid)

        return (outputs, hiddens)

    def guess(self, input_arr):

        inputs = Matrix.fromArray(input_arr)
        (outputs, _) = self.feedforward(inputs)

        return outputs.toArray()

    
    def train(self, input_arr, target_arr):
        
        inputs = Matrix.fromArray(input_arr)
        (outputs, hiddens) = self.feedforward(inputs)
        
        targets = Matrix.fromArray(target_arr)

        # Calculate the output error
        # ERROR = TARGETS - OUTPUTS
        output_errors = MatMath.subtract(targets, outputs)
        
        # Calculate output gradients
        output_gradients = MatMath.map(outputs, dsigmoid)
        output_gradients.multiply(output_errors)
        output_gradients.multiply(self.learning_rate)

        # Calculate deltas
        hiddens_T = MatMath.transpose(hiddens)
        weights_ho_deltas = MatMath.multiply(output_gradients, hiddens_T)

        # Adding deltas
        self.weights_ho.add(weights_ho_deltas)
        self.bias_o.add(output_gradients)

        # Calculate the hidden layer errors
        weights_ho_T = MatMath.transpose(self.weights_ho)
        hidden_errors = MatMath.multiply(weights_ho_T,output_errors)

        # Calculate hidden gradients
        hidden_gradients = MatMath.map(hiddens, dsigmoid)
        hidden_gradients.multiply(hidden_errors)
        hidden_gradients.multiply(self.learning_rate)

        # Calculate deltas
        inputs_T = MatMath.transpose(inputs)
        weights_ih_deltas = MatMath.multiply(hidden_gradients, inputs_T)

        # Adding deltas
        self.weights_ih.add(weights_ih_deltas)
        self.bias_h.add(hidden_gradients)