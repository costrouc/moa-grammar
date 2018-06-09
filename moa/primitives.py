"""This declares the MOA primitives in the abstract syntax tree

"""


class NDArray:
    def __init__(self, shape, data, constant=False):
        self._constant = constant
        self._shape = shape
        self._data = data

    @property
    def shape(self):
        return self._shape

    @property
    def data(self):
        return self._data

    def gamma(self, index):
        raise NotImplementedError()
