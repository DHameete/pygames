from matrix import Matrix

class MatMath:

    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        if(isinstance(a, Matrix)):
            m = a.copy()
        else:
            raise TypeError("Input 1 is not a Matrix Type")

        if(isinstance(b, Matrix)):
            if a.rows == b.rows and a.cols == b.cols:
                m.values = [[v1+v2 for (v1, v2) in zip(row1, row2)] for (row1, row2) in zip(a.values, b.values)]
            else:
                raise ValueError("Matrices do not have the same size.")
        else:
            raise TypeError("Input 2 is not a Matrix Type")

        return m

    @staticmethod
    def subtract(a, b):
        if(isinstance(a, Matrix)):
            m = a.copy()
        else:
            raise TypeError("Input 1 is not a Matrix Type")

        if(isinstance(b, Matrix)):
            if a.rows == b.rows and a.cols == b.cols:
                m.values = [[v1-v2 for (v1, v2) in zip(row1, row2)] for (row1, row2) in zip(a.values, b.values)]
            else:
                raise ValueError("Matrices do not have the same size.")
        else:
            raise TypeError("Input 2 is not a Matrix Type")

        return m

    @staticmethod
    def multiply(a, b):
        if(isinstance(a, Matrix)):
            pass
        else:
            raise TypeError("Input 1 is not a Matrix Type")

        if(isinstance(b, Matrix)):
            if a.cols == b.rows:
                m = Matrix(a.rows,b.cols)
                for i in range(a.rows):
                    for j in range(b.cols):
                        sum = 0
                        for k in range(a.cols):
                            sum += a.values[i][k] * b.values[k][j]
                        m.values[i][j] = sum
            else:
                raise ValueError("Matrices do not have the correct size.")
        else:
            raise TypeError("Input 2 is not a Matrix Type")

        return m

    @staticmethod
    def transpose(a):
        m = Matrix(a.cols, a.rows)
        m.values = list(map(list, zip(*a.values)))
        return m

    @staticmethod
    def map(a, func):
        m = a.copy()
        m.values = [[func(value) for value in row] for row in a.values]
        return m
