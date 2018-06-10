import pytest

from moa.primitives import NDArray, UnaryOperation, BinaryOperation, Function
from moa.yaccer import build_parser


@pytest.mark.parametrize("expression,result", [
    ("< 1 2 3>", NDArray(shape=(3,), data=[1, 2, 3], constant=False)),
])
def test_parse_vector(expression, result):
    parser = build_parser(start='vector')
    assert parser.parse(expression) == result


@pytest.mark.parametrize("expression, result", [
    ("const array A^3 <4 3 5>", NDArray(
        shape=(4, 3, 5), data=None, constant=True, identifier='A')),
])
def test_parse_constant_arrays(expression, result):
    parser = build_parser(start='constant_array')
    assert parser.parse(expression) == result


@pytest.mark.parametrize("expression, result", [
    ("array Zasdf_asdf^1 <3>", NDArray(
        shape=(3,), data=None, constant=False, identifier='Zasdf_asdf')),
])
def test_parse_arrays(expression, result):
    parser = build_parser(start='array')
    assert parser.parse(expression) == result


@pytest.mark.parametrize("expression, result", [
    ("j psi x", BinaryOperation(
        operator='PSI',
        left=NDArray(shape=None, data=None, constant=False, identifier='j'),
        right=NDArray(shape=None, data=None, constant=False, identifier='x'))),
    ("A omega <1 2>", BinaryOperation(
        operator='OMEGA',
        left=NDArray(shape=None, data=None, constant=False, identifier='A'),
        right=NDArray(shape=(2,), data=[1, 2], constant=False, identifier=None))),
    ("A omega B cat C", BinaryOperation(
        operator='OMEGA',
        left=NDArray(shape=None, data=None, constant=False, identifier='A'),
        right=BinaryOperation(
            operator='CAT',
            left=NDArray(shape=None, data=None, constant=False, identifier='B'),
            right=NDArray(shape=None, data=None, constant=False, identifier='C')
        ))),
    ("(A omega B) cat C", BinaryOperation(
        operator='CAT',
        left=BinaryOperation(
            operator='OMEGA',
            left=NDArray(shape=None, data=None, constant=False, identifier='A'),
            right=NDArray(shape=None, data=None, constant=False, identifier='B')),
        right=NDArray(shape=None, data=None, constant=False, identifier='C'))),
    ("dim A cat B", UnaryOperation( # binary gets preference over unary
        operator='DIM',
        right=BinaryOperation(
            operator='CAT',
            left=NDArray(shape=None, data=None, constant=False, identifier='A'),
            right=NDArray(shape=None, data=None, constant=False, identifier='B')))),
    ("dim (A cat B)", UnaryOperation(
        operator='DIM',
        right=BinaryOperation(
            operator='CAT',
            left=NDArray(shape=None, data=None, constant=False, identifier='A'),
            right=NDArray(shape=None, data=None, constant=False, identifier='B')))),
])
def test_parse_terms_and_operators(expression, result):
    parser = build_parser(start='term')
    assert parser.parse(expression) == result


@pytest.mark.parametrize("expression, result", [
    ('main(){}', Function(arguments=[], statements=[], identifier='main')),
    ('foo_bar(array A^1 <5>){}', Function(
        arguments=[NDArray(shape=(5,), data=None, constant=False, identifier='A')],
        statements=[],
        identifier='foo_bar')),
    ('BizBAZZ(array A^2 < 3 5>, array B^3 <6 5 8>){}', Function(
        arguments=[
            NDArray(shape=(3, 5), data=None, constant=False, identifier='A'),
            NDArray(shape=(6, 5, 8), data=None, constant=False, identifier='B')],
        statements=[],
        identifier='BizBAZZ')),
    ('A_2_3_a(array A^2 <9 1>, array B^2 <3 1>, array ASDF^1 <9>){}', Function(
        arguments=[
            NDArray(shape=(9, 1), data=None, constant=False, identifier='A'),
            NDArray(shape=(3, 1), data=None, constant=False, identifier='B'),
            NDArray(shape=(9,), data=None, constant=False, identifier='ASDF')],
        statements=[],
        identifier='A_2_3_a')),
])
def test_parse_function(expression, result):
    parser = build_parser(start='function')
    assert parser.parse(expression) == result
