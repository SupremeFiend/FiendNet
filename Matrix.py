"""

Simple tool for matrix operations

"""

import numpy as np

def AdditionError (mat1, mat2):
	print ("ADDITION ERROR !!")
	print ("CANNOT ADD / SUBTRACT THESE TWO:")
	print (mat1.matrix)
	print (mat2.matrix)

def MultiplicationError (mat1, mat2):
	print ("MULTIPLICATION ERROR !!")
	print ("CANNOT MULTIPLY THESE TWO:")
	print (mat1.matrix)
	print (mat2.matrix)

def HadamardError (mat1, mat2):
	print ("HADAMARD ERROR !!")
	print ("CANNOT HADAMARD THESE TWO:")
	print (mat1.matrix)
	print (mat2.matrix)

class Matrix:
	def __init__(self, numrows, numcols):
		self.rows = numrows
		self.cols = numcols
		self.matrix = []
		for i in range (self.rows):
			row = []
			for j in range (self.cols):
				row.append(0)
			
			self.matrix.append(row)
	
	def set_values (self, mat):
		for i in range (self.rows):
			for j in range (self.cols):
				self.matrix[i][j] = mat[i][j]
	
	def transpose (self):
		transmat = Matrix (self.cols, self.rows)
		
		for i in range(self.rows):
			for j in range(self.cols):
				transmat.matrix[j][i] = self.matrix[i][j]
		
		return transmat
		
	
	def add (self, mat2):
		addMat = Matrix(self.rows, self.cols)
		if self.rows == mat2.rows and self.cols == mat2.cols:
			for i in range (self.rows):
				for j in range (self.cols):
					addMat.matrix[i][j] = self.matrix[i][j] + mat2.matrix[i][j]
			return addMat
		
		else:
			AdditionError(self, mat2)
			exit()
		
	def subtract (self, mat2):
		subMat = Matrix(self.rows, self.cols)
		if self.rows == mat2.rows and self.cols == mat2.cols:
			for i in range (self.rows):
				for j in range (self.cols):
					subMat.matrix[i][j] = self.matrix[i][j] - mat2.matrix[i][j]
			return subMat
		else:
			AdditionError(self, mat2)
			exit()
		
		
	def multiply (self, mat2):
		mult = Matrix(self.rows, mat2.cols)
		
		if self.cols == mat2.rows:
			for i in range(len(self.matrix)):
				for j in range(len(mat2.matrix[0])):
					for k in range(len(mat2.matrix)):
						mult.matrix[i][j] += self.matrix[i][k]*mat2.matrix[k][j]
			
			return mult
		
		else:
			MultiplicationError(self, mat2)
			exit()
	
	def hadamard (self, mat2):
		had = Matrix(self.rows, self.cols)
		
		if self.rows == mat2.rows and self.cols == mat2.cols:
			for i in range (self.rows):
				for j in range(self.cols):
					hadamard[i][j] = self.matrix[i][j]*mat2.matrix[i][j]
					
			return had
		else:
			HadamardError(self, mat2)
			exit()
			
			
