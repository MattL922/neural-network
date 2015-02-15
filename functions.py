import math

def linear(x):
    return x

def sigmoid(x):
    return 1.0 / (1.0 + pow(math.e, -x))

def tanh(x):
    return (pow(math.e, 2*x) - 1) / (pow(math.e, 2*x) + 1)
