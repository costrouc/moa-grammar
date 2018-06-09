import pytest

from moa import (
    parser,
    NDArray, UnaryOperation, BinaryOperation
)

@pytest.mark.parametrize("expression,result", [
    ("< 1 2 3>", NDArray(shape=(3,), data=[1, 2, 3], constant=False)),
    ("const array A^3 <4 3 5>", NDArray(
        shape=(4, 3, 5), data=None, constant=True, identifier='A')),
    ("array Zasdf_asdf^1 <3>", NDArray(
        shape=(3,), data=None, constant=False, identifier='Zasdf_asdf')),
])
def test_parse_arrays(expression, result):
    assert parser.parse(expression) == result


@pytest.mark.parametrize("expression, result", [
    ("j psi x", BinaryOperation(
        operator='PSI',
        left=NDArray(shape=None, data=None, constant=False, identifier='j'),
        right=NDArray(shape=None, data=None, constant=False, identifier='x'))),
])
def test_parse_operators(expression, result):
    print('asdf', parser.parse(expression))
    assert parser.parse(expression) == result
