
from power import power_function
import pytest


def test_1():
    with pytest.raises(ValueError):
        power_function('45 2b +')


def test_2():
    with pytest.raises(ValueError):
        power_function('55 но +')


def test_3():
    with pytest.raises(ValueError):
        power_function('+ 45 89 +')


def test_4():
    with pytest.raises(ValueError):
        power_function('(8(4 5 +-))')


def test_5():
    with pytest.raises(ValueError):
        power_function('4 5 0 / +')


def test_6():
    with pytest.raises(ValueError):
        power_function('45 45 45')


def test_7():
    with pytest.raises(ValueError):
        power_function('45 45 45 ++++')


def test_8():
    with pytest.raises(ValueError):
        power_function('45 45 45 %+')


def test_9():
    assert power_function('45 2 +') == 47.0


def test_10():
    assert power_function('45 0.5 +') == 45.5


def test_11():
    assert power_function('(3 4 2 * 1 5 − 2 ^ / +)') == 3.5


def test_12():
    assert power_function('3 4 2 * 1 5 − 2 ^ / +') == 3.5


def test_13():
    assert power_function('4 5 0 + /') == 0.8


def test_14():
    assert power_function('(45 8 +) 7 +') == 60
