import math

class Linear(object):
    def __init__(self):
        pass

    def evaluate(self, x):
        return x

    def derivative(self, x):
        return 1

def sigmoid(x):
    return 1.0 / (1.0 + pow(math.e, -x))

class Tanh(object):
    """Hyperbolic tangent function"""

    def __init__(self):
        pass

    def evaluate(self, x):
        return (pow(math.e, 2*x) - 1) / (pow(math.e, 2*x) + 1)

    def derivative(self, x):
        return ((2*pow(math.e, 2*x)) / (pow(math.e, 2*x) + 1)) - ((2*pow(math.e, 4*x) - (2*pow(math.e, 2*x))) / pow(pow(math.e, 2*x) + 1, 2))
