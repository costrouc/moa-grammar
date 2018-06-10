import pytest

from moa import Function, NDArray, BinaryOperation
from moa.yaccer import build_parser


@pytest.mark.parametrize("filename,result", [
    ("test_files/moa/example0.moa", Function(
        identifier='test',
        arguments=[
            NDArray(shape=(5, 4), data=None, constant=False, identifier='A'),
            NDArray(shape=(4, 6), data=None, constant=False, identifier='C')],
        statements=[
            NDArray(shape=(2, 4), data=[1, 2, 3, 4, 1, 2, 3, 4], constant=True, identifier='B'),
            BinaryOperation(
                operator='EQUAL',
                left=NDArray(shape=None, data=None, constant=False, identifier='A'),
                right=BinaryOperation(
                    operator='CAT',
                    left=NDArray(shape=None, data=None, constant=False, identifier='B'),
                    right=BinaryOperation(
                        operator='DROP',
                        left=NDArray(shape=(2,), data=[1, 2], constant=False, identifier=None),
                        right=NDArray(shape=None, data=None, constant=False, identifier='C'),
                    )
                )
            )
        ])),
])
def test_parse_vector(filename, result):
    with open(filename) as f:
        contents = f.read()
    parser = build_parser()
    #assert parser.parse(contents) == result
