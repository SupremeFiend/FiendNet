"""

Testing FiendNet

"""


from FiendNet import Network
from Matrix import Matrix


nn = Network(2, 4, 3)

nn.inputs.set_values([[1, 0]])

nn.feedforward()

nn.print_network()
