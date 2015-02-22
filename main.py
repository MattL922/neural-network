from networks.network import *
from neurons import *
from parsers.parser import *
from functions import *

parser = Parser("data.csv")
network = Network(parser)
return_input_neuron = InputNeuron(Linear())
volume_ratio_input_neuron = InputNeuron(Linear())
input_bias = BiasNeuron()
hidden_neuron1 = HiddenNeuron(Tanh())
#hidden_neuron2 = HiddenNeuron(Tanh())
hidden_bias = BiasNeuron()
output_neuron = OutputNeuron(Tanh())
network.add_input_neuron("return", return_input_neuron)
network.add_input_neuron("volume-ratio", volume_ratio_input_neuron)
network.add_hidden_neuron(hidden_neuron1)
#network.add_hidden_neuron(hidden_neuron2)
network.add_output_neuron(output_neuron)
network.add_input_neuron("bias", input_bias)
network.add_hidden_neuron(hidden_bias)
network.connect()
network.train()
