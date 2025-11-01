
from src.power import main_function
from src.bracket import bracket_analize
from src.calculate import calcul
from src.errors import CorrectionError
from src.errors import SymbolError
from src.errors import BracketError

import pytest


def test_1():
    with pytest.raises(SymbolError):
        main_function('45 2b +')


def test_2():
    with pytest.raises(SymbolError):
        main_function('55 но +')


def test_3():
    with pytest.raises(ValueError):
        main_function('+ 45 89 +')


def test_4():
    with pytest.raises(BracketError):
        main_function('(8(4 5 +-))')


def test_5():
    with pytest.raises(ZeroDivisionError):
        main_function('4 5 0 / +')


def test_6():
    with pytest.raises(ValueError):
        main_function('45 45 45')


def test_7():
    with pytest.raises(CorrectionError):
        main_function('45 45 45 ++++')


def test_8():
    with pytest.raises(CorrectionError):
        main_function('45 45 45 %+')

def test_9():
    with pytest.raises(CorrectionError):
        main_function('1.1.1 4 +')

def test_10():
    assert main_function('45 2 +') == 47.0


def test_11():
    assert main_function('45 0.5 +') == 45.5


def test_12():
    assert main_function('(1 2 +) (4 5 +) *') == 27.0


def test_13():
    assert main_function('4 5 0 + /') == 0.8


def test_14():
    assert main_function('(45 8 +) 7 +') == 60
