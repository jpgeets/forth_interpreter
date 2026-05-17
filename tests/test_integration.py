from forth_interpreter import Interpreter


def test_empty_input_returns_empty_stack():
    interpreter = Interpreter()
    result = interpreter.execute("   ")
    assert result == []


def test_comments_do_not_affect_execution():
    interpreter = Interpreter()
    result interpreter.execute("6 2 + ( add ) 3 +")
    assert  result == [11]
