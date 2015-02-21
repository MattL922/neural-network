class Network(object):
    """Network"""

    def __init__(self, parser=None, learning_rate=0.5):
        self.parser = parser
        self.input_layer = []
        self.hidden_layer = []
        self.output_layer = []
        self.learning_rate = learning_rate

    def add_input_neuron(self, neuron):
        self.input_layer.append(neuron)

    def add_hidden_neuron(self,neuron):
        self.hidden_layer.append(neuron)

    def add_output_neuron(self, neuron):
        self.output_layer.append(neuron)

    def run(self):
        for data in self.parser.parse():
            for neuron in self.input_layer:
                neuron.receive(data["return"])
                neuron.activate()
            for neuron in self.hidden_layer:
                neuron.activate()
            for neuron in self.output_layer:
                neuron.activate()

    def train(self):
        for data in self.parser.parse():
            output = None
            # run the forward propagation
            for neuron in self.input_layer:
                neuron.receive(data["return"])
                neuron.activate()
            for neuron in self.hidden_layer:
                neuron.activate()
            for neuron in self.output_layer:
                output = neuron.activate()
            # run the backward propagation
            target = data["target"]
            print output, target
            for neuron in self.output_layer:
                neuron.calculate_delta(target)
            for neuron in self.hidden_layer:
                neuron.calculate_delta()
            for neuron in self.input_layer:
                for connection in neuron.forward_connections:
                    connection.weight += (-1 * self.learning_rate * connection.neuron.delta * neuron.output_value)
            for neuron in self.hidden_layer:
                for connection in neuron.forward_connections:
                    connection.weight += (-1 * self.learning_rate * connection.neuron.delta * neuron.output_value)

    def connect(self):
        for hidden_neuron in self.hidden_layer:
            for output_neuron in self.output_layer:
                hidden_neuron.add_forward_connection(output_neuron)
        for input_neuron in self.input_layer:
            for hidden_neuron in self.hidden_layer:
                input_neuron.add_forward_connection(hidden_neuron)
