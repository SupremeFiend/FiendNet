from FiendNet import Network


lr = 0.05
epochs = 2000

init_inputs = [0, 0]
init_hidden = [0, 0, 0, 0]
init_outputs = [0, 0, 0, 0]

input_set = [[0, 0], [0, 1], [1, 0], [1, 1]]
label_set = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


nn = Network(init_inputs= init_inputs, hidden = init_hidden, init_outputs= init_outputs)

nn.gradient_descent_train(lr, input_set, label_set, epochs)

#nn.draw_network()


print()
print()

print(nn.feedforward([1, 0]).matrix) 
