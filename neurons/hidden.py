from neurons.Neuron import *
from collections import deque

class HiddenNeuron(Neuron):
    """Hidden neuron"""

    def __init__(self):
        self.neurons = []
        self.input_signals = deque()

    def activate(self):
        try:
            prev_value, cur_value = self.input_signals.popleft()
            if cur_value > prev_value:
                self.emit(1.0)
            elif cur_value < prev_value:
                self.emit(-1.0)
            else:
                self.emit(0.0)
        except IndexError:
            print "No input signals to process"

    def emit(self, output_signal):
        for neuron in self.neurons:
            neuron.receive(output_signal)

    def receive(self, input_signal):
        self.input_signals.append(input_signal)

    def add_connection(self, neuron):
        self.neurons.append(neuron)
