from forth_interpreter.interpreter import Interpreter

def test_addition():
    interpreter = Interpreter()
    result = interpreter.execute("3 4 +")
    assert result == [7]

def test_subtraction():
    interpreter = Interpreter()
    result = interpreter.execute("8 5 -")
    assert result == [3]

def test_negative_number():
    interpreter = Interpreter()
    result = interpreter.execute("-5 3 +")
    assert result == [-2]
