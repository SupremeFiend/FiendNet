"""

FiendNet

ULTRA simple neural network library.
Essentially, a toy for fooling around with neural nets

***

Only one hidden layer.
Only feed-forward possible. Backpropagation has to be done using external code.

***

This is intended to be used with many optimisation techniques, not just gradient descent.

Enjoy :)

***

Author : Pranay Venkatesh (SupremeFiend)

"""

from Matrix import Matrix
import numpy as np
import matplotlib.pyplot as plt
import random


def sigmoid(mat):
	mat2 = mat
	for i in range (len(mat.matrix[0])):
		mat2.matrix[0][i] = 1/(1 + np.exp(-mat.matrix[0][1]))
	
	return mat2
	
def randomise(mat):
	for i in range (mat.rows):
		for j in range (mat.cols):
			mat.matrix[i][j] = random.uniform(0,1)

def softmax (mat):
	sumexps = 0
	for i in range(len(mat.matrix[0])):
		sumexps += np.exp(mat.matrix[0][i])
	
	for ele in mat.matrix[0]:
		ele = ele/sumexps
	return mat

class Network:
	
	def __init__(self, inp_length, hid_length, out_length):
		self.inp_size = inp_length
		self.hid_size = hid_length
		self.out_size = out_length
		self.inputs = Matrix(1, inp_length)
		self.hidden = Matrix(1, hid_length)
		self.outputs = Matrix(1, out_length)
		self.weights_ih = Matrix (inp_length, hid_length)
		self.weights_ho = Matrix (hid_length, out_length)
		randomise(self.weights_ih)
		randomise(self.weights_ho)
		
	def feedforward(self):
		self.hidden = self.inputs.multiply(self.weights_ih)
		self.hidden = sigmoid(self.hidden)
		self.outputs = softmax(self.hidden.multiply(self.weights_ho))
		

	def print_network(self):
		print(self.inputs.matrix)
		print()
		print()
		print(self.weights_ih.matrix)
		print()
		print()		
		print(self.hidden.matrix)
		print()
		print()
		print(self.weights_ho.matrix)
		print()
		print()
		print(self.outputs.matrix)
			
	
