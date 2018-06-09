"""This declares the MOA primitives in the abstract syntax tree

"""


class NDArray:
    def __init__(self, shape, data, constant=False, identifier=None):
        self.shape = shape
        self.data = data
        self.constant = constant
        self.identifier = identifier

    def gamma(self, index):
        raise NotImplementedError()


class UnaryOperation:
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right


class BinaryOperation:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right
