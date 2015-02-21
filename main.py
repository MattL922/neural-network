from networks.network import *
from neurons import *
from parsers.parser import *
from functions import *

parser = Parser("data.csv")
network = Network(parser)
input_neuron = InputNeuron(Linear())
input_bias = BiasNeuron()
hidden_neuron = HiddenNeuron(Tanh())
hidden_bias = BiasNeuron()
output_neuron = OutputNeuron(Tanh())
network.add_input_neuron(input_neuron)
network.add_hidden_neuron(hidden_neuron)
network.add_output_neuron(output_neuron)
network.add_input_neuron(input_bias)
network.add_hidden_neuron(hidden_bias)
network.connect()
network.train()
