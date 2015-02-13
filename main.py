from network.Network import *
from neurons.InputNeuron import *
from neurons.HiddenNeuron import *
from neurons.OutputNeuron import *
from parsers.Parser import *

network = Network()
input_neuron = InputNeuron()
hidden_neuron = HiddenNeuron()
output_neuron = OutputNeuron()
network.add_input_neuron(input_neuron)
network.add_hidden_neuron(hidden_neuron)
network.add_output_neuron(output_neuron)
network.connect()
parser = Parser("data.csv")
for record in parser.parse():
    network.receive(record)
