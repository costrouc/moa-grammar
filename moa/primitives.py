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

    def __eq__(self, other):
        return (
            self.shape == other.shape and \
            self.constant == other.constant and \
            self.identifier == other.identifier and \
            type(self.data) == type(other.data) and \
            self.data == other.data
        )

    def __repr__(self):
        return f'{self.identifier}(const={self.constant}, shape={self.shape}, data={self.data})'

    def __str__(self):
        return self.__repr__()


class UnaryOperation:
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

    def __eq__(self, other):
        return (self.operator == other.operator and \
                self.right == self.right)

    def __repr__(self):
        return f'{self.operator} {self.right}'

    def __str__(self):
        return self.__repr__()


class BinaryOperation:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (self.operator == other.operator and \
                self.left == other.left and \
                self.right == other.right)

    def __repr__(self):
        return f'({self.left}) {self.operator} ({self.right})'

    def __str__(self):
        return self.__repr__()


class Function:
    def __init__(self, arguments, statements, identifier):
        self.arguments = arguments
        self.statements = statements
        self.identifier = identifier

    def __eq__(self, other):
        return (self.arguments == other.arguments and \
                self.statements == other.statements and \
                self.identifier == other.identifier)

    def __repr__(self):
        return f'f({self.arguments}){{ {self.statements} }}'

    def __str__(self):
        return self.__repr__()
