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
def test_parse_filename_resulting_ast(filename, result):
    with open(filename) as f:
        contents = f.read()
    parser = build_parser()
    assert parser.parse(contents) == result


@pytest.mark.parametrize("filename", [
    "test_files/moa/example0.moa",
    "test_files/moa/example1.moa",
    "test_files/moa/example2.moa",
    # "test_files/moa/example3.moa", # omega not handled properly
    "test_files/moa/example4.moa",
    # "test_files/moa/example5.moa", # int in file
    # "test_files/moa/example6.moa", # int in file
    # "test_files/moa/example7.moa", # omega not handled properly
    "test_files/moa/example8.moa",
    "test_files/moa/example9.moa",
    # "test_files/moa/lu.moa", # int, for loop in file
    # "test_files/moa/mm.moa", # int, brackets in file and omega not handled properly
    # "test_files/moa/ops.moa", # omega not handled properly
    "test_files/moa/tmp.moa"
])
def test_parse_filenames(filename):
    with open(filename) as f:
        contents = f.read()
    parser = build_parser()
    parser.parse(contents) # not checking ast for now
