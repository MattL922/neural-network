from random import gauss

class Connection(object):
    """Connects one neuron to another with a weight"""

    def __init__(self, neuron=None):
        self.neuron = neuron
        self.weight = gauss(0, 1)

    def emit(self, value):
        self.neuron.receive(value * self.weight)
