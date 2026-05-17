from forth_interpreter import Interpreter


def test_addition():
    interpreter = Interpreter()
    result = interpreter.execute("3 4 +")
    assert result == [7]


def test_subtraction_preserves_forth_order():
    interpreter = Interpreter()
    result = interpreter.execute("8 5 -")
    assert result == [3]


def test_negative_number():
    interpreter = Interpreter()
    result = interpreter.execute("-5 3 +")
    assert result == [-2]


def test_multiple_operations():
    interpreter = Interpreter()
    result = interpreter.execute("10 3 - 2 +")
    assert result == [9]
