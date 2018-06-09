import pytest

from moa import parser, NDArray

@pytest.mark.parametrize("expresion,result", [
    ("< 1 2 3>", NDArray(shape=(3,), data=[1, 2, 3], constant=False)),
])
def test_parse_vector(expresion, result):
     result = parser.parse(expresion)
     print(result)
     assert result == result
