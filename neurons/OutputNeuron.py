from neurons.Neuron import *
from collections import deque

class OutputNeuron(Neuron):
    """Output neuron"""

    def __init__(self):
        self.input_signals = deque()

    def activate(self):
        try:
            input_signal = self.input_signals.popleft()
            if input_signal > 0:
                self.emit("UP ({0})".format(input_signal))
            elif input_signal < 0:
                self.emit("DOWN ({0})".format(input_signal))
            else:
                self.emit("UNCH ({0})".format(input_signal))
        except IndexError:
            print "No input signals to process"

    def emit(self, output_signal):
        print output_signal

    def receive(self, input_signal):
        self.input_signals.append(input_signal)
