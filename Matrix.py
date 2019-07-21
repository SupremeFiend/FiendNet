import numpy as np
import random

def dot (row1, row2):
    dotted = 0
    for i in range (len(row1)):
        dotted += row1[i]*row2[i]
    return dotted

class Matrix:

    def __init__(self, numrows, numcolumns):
        self.matrix = []
        self.rows = numrows
        self.cols = numcolumns
        for i in range (self.rows):
            row = []
            for j in range (self.cols):
                row.append(random.randint(0, 9))
            self.matrix.append(row)

    def set_values(self, valuemat):
        i = 0
        while i < self.rows:
            j = 0
            while j < self.cols:
                self.matrix[i][j] = valuemat[i][j]
                j += 1
            i += 1
        return self

    def add(self, mat2):
        added = Matrix(self.rows, self.cols)
        if self.rows != mat2.rows or self.cols != mat2.cols:
            print("MATRIX ADDITION ERROR")
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    added.matrix[i][j] = self.matrix[i][j] - mat2.matrix[i][j]
            return added
        
    def subtract (self, mat2):
        subbed = Matrix(self.rows, self.cols)
        if self.rows != mat2.rows or self.cols != mat2.cols:
            print ("MATRIX SUBTRACTION ERROR")

        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    subbed.matrix[i][j] = self.matrix[i][j] - mat2.matrix[i][j]

            return subbed

    def transpose_mat(self):
        transed = Matrix(self.cols, self.rows)
        for i in range (self.rows):
            for j in range(self.cols):
                transed.matrix[j][i] = self.matrix[i][j]
                
        return transed


        
    def multiply(self, mat2):
        #print (self.matrix)
        #print (mat2.matrix)
        multed = Matrix(self.rows, mat2.cols)
        #if self.cols != mat2.rows:
            #print ("MATRIX MULTIPLICATION ERROR")
        for i in range(self.rows):
                for j in range(mat2.cols):
                    multed.matrix[i][j] = 0
                    for k in range(mat2.rows):
                        multed.matrix[i][j] += self.matrix[i][k] * mat2.matrix[k][j]
        #print(multed.matrix)
        return multed
        #else:
            #pass
        
    def hadamard_product(self, mat2):
        multed = Matrix(self.rows, self.cols)
        if self.rows != mat2.rows or self.cols != mat2.cols:
            print ("HADAMARD PRODUCT ERROR")

        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    multed.matrix[i][j] = self.matrix[i][j]*mat2.matrix[i][j]
            return multed

        
