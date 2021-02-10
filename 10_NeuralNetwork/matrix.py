import random

class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = []

        self.values = [ [0]*self.cols for _ in range(self.rows) ]

    def add(self, n):
        if(isinstance(n, Matrix)):
            if self.rows == n.rows and self.cols == n.cols:
                self.values = [[v1+v2 for (v1, v2) in zip(row1, row2)] for (row1, row2) in zip(self.values, n.values)]
            else:
                raise ValueError("Matrices do not have the same size.")
        elif(isinstance(n, (float, int, complex))):
            self.values = [[col + n for col in row] for row in self.values]
        else:
            raise TypeError("Input is not a Numeric Type")


    def dot(self):
        pass

    def transpose(self):
        pass

    def randomize(self):
        self.values = [[random.randrange(10) for col in row] for row in self.values]
