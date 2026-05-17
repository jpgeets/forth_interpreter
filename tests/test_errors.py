import pytest

from forth_interpreter import Interpreter, StackUnderflowError, UnknownTokenError


def test_unknown_token_raises_custom_error():
    interpreter = Interpreter()

    with pytest.raises(UnknownTokenError):
        interpreter.execute("3 nope")


def test_addition_requires_two_values():
    interpreter = Interpreter()

    with pytest.raises(StackUnderflowError):
        interpreter.execute("3 +")


def test_subtraction_requires_two_values():
    interpreter = Interpreter()

    with pytest.raises(StackUnderflowError):
        interpreter.execute("-")
