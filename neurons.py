from collections import deque
from random import gauss

class Neuron(object):
    """Neuron class"""

    def __init__(self, func=None):
        self.neurons = []
        self.input_signals = deque()
        self.value = 0.0
        self.weight = gauss(0, 1)
        self.func = func

    def activate(self):
        self.value = self.func(sum(self.input_signals)) * self.weight
        self.input_signals.clear()
        self.emit(self.value)

    def emit(self, output_signal):
        for neuron in self.neurons:
            neuron.receive(output_signal)

    def receive(self, input_signal):
        self.input_signals.append(input_signal)

    def add_connection(self, neuron):
        self.neurons.append(neuron)

class InputNeuron(Neuron):
    """Input neuron"""

    def __init__(self, func=None):
        super(InputNeuron, self).__init__(func)

class HiddenNeuron(Neuron):
    """Hidden neuron"""

    def __init__(self, func=None):
        super(HiddenNeuron, self).__init__(func)

class OutputNeuron(Neuron):
    """Output neuron"""

    def __init__(self, func=None):
        super(OutputNeuron, self).__init__(func)

    def emit(self, output_signal):
        print output_signal

class BiasNeuron(Neuron):
    """Bias neuron"""

    def __init__(self, value=1.0):
        super(BiasNeuron, self).__init__()
        self.value = value
        self.weight = gauss(0, 1)

    def activate(self):
        self.emit(self.value * self.weight)

    def receive(self, input_signal):
        pass # bias neurons don't need input
