import pytest

from averages import round_to_half, weighted_average


def test_weighted_average():
    result = weighted_average([(5.0, 1.0), (4.0, 2.0)])
    assert result == pytest.approx(4.33, abs=0.005)


def test_weighted_average_without_grades():
    assert weighted_average([]) is None


@pytest.mark.parametrize("value, expected", [(4.25, 4.5), (4.24, 4.0), (5.75, 6.0)])
def test_round_to_half(value, expected):
    assert round_to_half(value) == expected
