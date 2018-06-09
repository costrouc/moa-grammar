import pytest

from moa import NDArray


def test_empty_ndarray():
    array = NDArray(shape=(), data=[])

    # Ensuring specific implementation
    assert len(array.shape) == 0
    assert array.shape == ()
    assert len(array.data) == 0
    assert array.data == []
