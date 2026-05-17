import pytest

from forth_interpreter.errors import StackUnderflowError
from forth_interpreter.stack import Stack


def test_stack_push_pop():
    stack = Stack()
    stack.push(10)
    stack.push(20)

    assert stack.pop() == 20
    assert stack.pop() == 10


def test_stack_peek_with_depth():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.peek() == 30
    assert stack.peek(1) == 20
    assert stack.peek(2) == 10


def test_stack_underflow_on_pop():
    stack = Stack()

    with pytest.raises(StackUnderflowError):
        stack.pop()


def test_stack_to_list_returns_copy():
    stack = Stack()
    stack.push(1)

    values = stack.to_list()
    values.append(99)

    assert stack.to_list() == [1]
