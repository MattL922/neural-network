from networks.network import *
from neurons.input import *
from neurons.hidden import *
from neurons.output import *
from parsers.parser import *

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
