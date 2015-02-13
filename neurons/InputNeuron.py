from collections import deque

class InputNeuron(Neuron):
    """Input neuron"""

    def __init__(self):
        self.prev_value = None
        self.neurons = []
        self.input_signals = deque()

    def activate(self):
        try:
            cur_value = self.input_signals.popleft()["close"]
            output_signal = (self.prev_value, cur_value)
            self.prev_value = cur_value
            self.emit(output_signal)
        except IndexError:
            print "No input signals to process"

    def emit(self, output_signal):
        for neuron in self.neurons:
            neuron.receive(output_signal)

    def receive(self, input_signal):
        self.input_signals.append(input_signal)
