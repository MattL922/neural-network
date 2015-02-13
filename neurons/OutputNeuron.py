from collections import deque

class OutputNeuron(Neuron):
    """Output neuron"""

    def __init__(self):
        self.input_signals = deque()

    def activate(self):
        try:
            emit(self.input_signals.popleft())
        except IndexError:
            print "No input signals to process"

    def emit(self, output_signal):
        print output_signal

    def receive(self, input_signal):
        self.input_signals.append(input_signal)
