import random

class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = []

        self.values = [ [0]*self.cols for _ in range(self.rows) ]

    def __str__(self):
        p = ''
        for row in self.values:
            p += f'{row}'
            p += '\n' 
        return p

    def add(self, n):
        if(isinstance(n, Matrix)):
            if self.rows == n.rows and self.cols == n.cols:
                self.values = [[v1+v2 for (v1, v2) in zip(row1, row2)] for (row1, row2) in zip(self.values, n.values)]
            else:
                raise ValueError("Matrices do not have the same size.")
        elif(isinstance(n, (float, int, complex))):
            self.values = [[value+n for value in row] for row in self.values]
        else:
            raise TypeError("Input is not a Numeric Type")
        
    def multiply(self, n):
        if(isinstance(n, Matrix)):
            if self.cols == n.rows:
                result = Matrix(self.rows, n.cols)
                for i in range(self.rows):
                    for j in range(n.cols):
                        total = 0
                        for k in range(self.cols):
                            total += self.values[i][k] * n.values[k][j]
                        result.values[i][j] = total
                return result
            else:
                raise ValueError("Matrices do not have the right size.")
        elif(isinstance(n, (float, int, complex))):
            self.values = [[value*n for value in row] for row in self.values]
        else:
            raise TypeError("Input is not a Numeric Type")

    def randomize(self):
        self.values = [[random.randrange(10) for _ in row] for row in self.values]

    def transpose(self):
        self.rows, self.cols = self.cols, self.rows
        self.values = list(map(list, zip(*self.values)))