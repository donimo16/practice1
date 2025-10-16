from app.src.calculator import Calculater

cal = Calculator()

def test_addition():
    assert cal.addition(1, 1) == 2
    assert cal.addition(1, 2) == 3

def test_subtraction():
    assert cal.subtraction(3, 1) == 2
    assert cal.subtraction(5, 1) == 4

def test_multiplication():
    assert cal.multiplication(4,8) == 32
