from forth_interpreter import Interpreter


def test_empty_input_returns_empty_stack():
    interpreter = Interpreter()
    assert interpreter.execute("   ") == []


def test_comments_do_not_affect_execution():
    interpreter = Interpreter()
    assert interpreter.execute("6 2 - ( subtract ) 3 +") == [7]
