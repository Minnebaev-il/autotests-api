import pytest


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_number_1(number: int):
    assert number > 0
