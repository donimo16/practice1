from app.src.calculator import Calculator

cal = Calculator()

def test_addition():
    assert cal.addition(2, 4) == 6
    assert cal.subtraction(9,3) == 6
    assert cal.multiplication(3, 5) == 15
    assert cal.devision(9, 3) == 3
