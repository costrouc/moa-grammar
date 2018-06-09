import pytest


class TestingHelpers:
    @staticmethod
    def assert_ndarray_allclose(a1, a2, tollerance=1e-8):
        assert a1.shape == a2.shape
        assert a1.constant == a2.constant
        assert a1.identifier == a2.identifier
        assert type(a1.data) == type(a2.data)
        if isinstance(a1.data, list):
            assert all([abs(e1 - e2) < tollerance for e1, e2 in zip(a1.data, a2.data)])
        else:
            assert a1.data == a2.data == None



@pytest.fixture
def helpers():
    return TestingHelpers
