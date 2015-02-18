from connections import *
from collections import deque
from random import gauss

class Neuron(object):
    """Neuron class"""

    def __init__(self, func=None):
        self.forward_connections = []
        self.input_signals = deque()
        self.value = 0.0
        self.func = func
        self.delta = 0.0

    def activate(self):
        self.value = self.func(sum(self.input_signals))
        self.input_signals.clear()
        self.emit()

    def emit(self):
        for connection in self.forward_connections:
            connection.emit(self.value)

    def receive(self, input_signal):
        self.input_signals.append(input_signal)

    def add_forward_connection(self, neuron):
        self.forward_connections.append(Connection(neuron))

    def calculate_delta(self, target):
        if(len(self.forward_connections) == 0):
            self.delta = target - self.value
        else:
            self.delta = 0.0
            for connection in self.forward_connections:
                self.delta += (connection.neuron.delta * connection.weight)

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

    def emit(self):
        print self.value

class BiasNeuron(Neuron):
    """Bias neuron"""

    def __init__(self, value=1.0):
        super(BiasNeuron, self).__init__()
        self.value = value

    def activate(self):
        self.emit()

    def receive(self, input_signal):
        pass # bias neurons don't need input
