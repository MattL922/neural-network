class Neuron(object):
    """Abstract neuron class"""

    def __init__(self):
        pass

    def activate(self, record):
        raise NotImplementedError("activate function not implemented!")

    def emit(self, output):
        raise NotImplementedError("emit not implemented!")

    def receive(self, input):
        raise NotImplementedError("receive not implemented!")

    def add_connection(self, neuron):
        raise NotImplementedError("receive not implemented!")
