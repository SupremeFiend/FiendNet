"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

FIENDNET

A homemade Neural Network library meant for simple tasks


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

I made this because I wanted to do something with neural nets and I was too lazy to learn TensorFlow
Also, I wanted to properly understand the proper funda behind neural networks rather than just use some arbitrary functions in some library


Author : Pranay Venkatesh (SupremeFiend)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""



from Matrix import Matrix
import numpy as np
import pygame


pygame.init()
win = pygame.display.set_mode((200, 200))
pygame.display.set_caption("FiendNet Neural Network")

def activation(x):
    return 1/(1 + np.exp(-x))

def d_activation(x):
    return activation(x)*(1-activation(x))

def activate_row(row):
    new_row = []
    for ele in row:
        new_row.append(activation(ele))
    return new_row

def activate_der_row(row):
    new_row = []
    for ele in row:
        new_row.append(d_activation(ele))
    return new_row

def array_sum(arr):
    s = 0
    for ele in arr:
        s += ele
    return s

class Network:
    def __init__(self, init_inputs, hidden, init_outputs):
        self.input_nodes = init_inputs
        self.hidden = hidden
        self.outputs = init_outputs
        self.weights_ih = Matrix(len(hidden), len(init_inputs))
        self.weights_ho = Matrix(len(init_outputs), len(hidden))
        self.bias_i = Matrix (1, len(hidden))
        self.bias_o = Matrix (1, len(init_outputs))

    def refresh_drawing(self):
        dx_inputs = 40
        dy_inputs = 40
        for i in range(len(self.input_nodes)):
            pygame.draw.circle(win, (255, 246, 143), (dx_inputs, dy_inputs), 30)
            dy_inputs += 60

        dx_hidden = 120
        dy_hidden = 40
        for i in range (len(self.hidden)):
            pygame.draw.circle(win, (255, 246, 143), (dx_hidden, dy_hidden), 30)
            dy_hidden += 60

        dx_output = 200
        dy_output = 40
        for i in range(len(self.outputs.matrix[0])):
            pygame.draw.circle(win, (255, 246, 143), (dx_output, dy_output), 30)
            dy_output += 60

    def draw_network(self):
        while True:
            pygame.display.update()
            self.refresh_drawing()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
            
    def feedforward(self, inp):
        #Feedforward into hidden layer
        self.input_nodes = inp     
        inp = [inp]
        input_set = Matrix(len(inp), 1)
        input_set.set_values(inp)
        h = self.weights_ih.multiply(input_set)
        h = h.transpose_mat()
        h = h.add(self.bias_i)
        h.matrix[0] = activate_row(h.matrix[0])
        
        #Feedforward into output layer
        self.outputs = h.multiply(self.weights_ho)
        
        self.outputs = self.outputs.add(self.bias_o)
        self.outputs.matrix[0] = activate_row(self.outputs.matrix[0])
        self.hidden = h.matrix

        return self.outputs

    def differential_h(self, inp):
        inp = [inp]
        input_set = Matrix(len(inp), 1)
        input_set.set_values(inp)
        h = self.weights_ih.multiply(input_set)
        h = h.transpose_mat()
        h = h.add(self.bias_i)
        return activate_der_row(h.matrix[0])

    def differential_z(self, inp):
        inp = [inp]
        input_set = Matrix(len(inp), 1)
        input_set.set_values(inp)
        h = self.weights_ih.multiply(input_set)
        h = h.transpose_mat()        
        h = h.add(self.bias_i)
        h.matrix[0] = activate_row(h.matrix[0])
        o = h.multiply(self.weights_ho)
        o = self.outputs.add(self.bias_o)
        o.matrix[0] = activate_row(o.matrix[0])
        return [activate_der_row(o.matrix[0])]

    
    def gradient_descent_train(self, learning_rate, input_set, label_set, epochs):
        for epoch in range(epochs):
            for i in range (len(input_set)):
                inputs = input_set[i]
                labels = label_set[i]
                self.input_nodes = inputs
                out = self.feedforward(self.input_nodes)

                # Backpropagation with Gradient Descent.
        
                error = []
                for j in range(out.cols):
                    error.append(labels[j] - out.matrix[0][j])
                print(array_sum(error))
                err_mat = Matrix(1, len(error))
                err_mat.set_values([error])
                err_matT = err_mat.transpose_mat()

                # Chaging weights and biases of hidden -> output layers
                                
                diff_z = self.differential_z(self.input_nodes)
                diff_z_mat = Matrix(1, len(diff_z[0]))
                diff_z_mat.set_values(diff_z)
                gradients = err_mat.hadamard_product(diff_z_mat)
                h_mat = Matrix(1, len(self.hidden[0]))
                #print(self.hidden)
                temp = []
                for i in range(len(self.hidden[0])):
                    temp.append(learning_rate*self.hidden[0][i])
                temp = [temp]
                h_mat.set_values(temp)
                del_wo = h_mat.transpose_mat().multiply(gradients)
                self.weights_ho = self.weights_ho.add(del_wo)
                self.bias_o = self.bias_o.add(gradients)

               # Changing weights and biases of input -> hidden layers

                w_ho_T = self.weights_ho.transpose_mat()
                hidden_errors = err_mat.multiply(w_ho_T)

                hidden_T = hidden_errors.transpose_mat()
                
                hg = self.differential_h(self.input_nodes)
                hidden_gradient = Matrix(1, len(hg))
                hidden_gradient.set_values([hg])

                hidden_gradient = hidden_gradient.hadamard_product(hidden_errors)

                inputs = Matrix(1, len(self.input_nodes))
                inputs.set_values([self.input_nodes])

                inp_T = inputs.transpose_mat()
                delta_ih = inp_T.multiply(hidden_gradient)
                delta_ih = delta_ih.transpose_mat()
                self.weights_ih = self.weights_ih.add(delta_ih)
                
                self.bias_i = self.bias_i.add(hidden_gradient)

