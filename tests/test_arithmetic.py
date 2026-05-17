from forth_interpreter import Interpreter

def test_addition():
    interpreter = Interpreter()
    result = interpreter.execute("3 4 +")
    assert result == [7]

def test_multiple_operations():
    interpreter = Interpreter()
    result = interpreter.execute("10 3 2 + +")
    assert result == [15]

def test_addition_with_negative_number():
    interpreter = Interpreter()
    result = interpreter.execute("-5 3 +")
    assert result == [-2]
