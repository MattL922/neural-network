from networks.network import *
from neurons import *
from parsers.parser import *
import functions

parser = Parser("data.csv")
network = Network(parser)
input_neuron = InputNeuron(functions.linear)
input_bias = BiasNeuron()
hidden_neuron = HiddenNeuron(functions.tanh)
hidden_bias = BiasNeuron()
output_neuron = OutputNeuron(functions.tanh)
network.add_input_neuron(input_neuron)
network.add_input_neuron(input_bias)
network.add_hidden_neuron(hidden_neuron)
network.add_hidden_neuron(hidden_bias)
network.add_output_neuron(output_neuron)
network.connect()
network.run()
