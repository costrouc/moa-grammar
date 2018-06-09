import pytest

from moa import parser, NDArray

@pytest.mark.parametrize("expresion,result", [
    ("< 1 2 3>", NDArray(shape=(3,), data=[1, 2, 3], constant=False)),
    ("const array A^3 <4 3 5>", NDArray(
        shape=(4, 3, 5), data=None, constant=True, identifier='A')),
    ("array Zasdf_asdf^1 <3>", NDArray(
        shape=(3,), data=None, constant=False, identifier='Zasdf_asdf')),
])
def test_parse_vector(expresion, result, helpers):
     eval_result = parser.parse(expresion)
     helpers.assert_ndarray_allclose(eval_result, result)
