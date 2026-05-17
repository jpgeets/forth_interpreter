"""Core interpreter implementation."""

from __future__ import annotations

from .errors import UnknownTokenError
from .parser import is_integer_token, parse_integer, tokenize
from .stack import Stack


class Interpreter:
    """Small Forth-like interpreter.

    Current supported words:
    - integer literals
    - +
    - -
    """

    def execute(self, code: str) -> list[int]:
        stack = Stack()

        for token in tokenize(code):
            if is_integer_token(token):
                stack.push(parse_integer(token))
            elif token == "+":
                stack.require_depth(2)
                a = stack.pop()
                b = stack.pop()
                stack.push(a + b)
            elif token == "-":
                stack.require_depth(2)
                a = stack.pop()
                b = stack.pop()
                stack.push(a - b)
            else:
                raise UnknownTokenError(f"Unknown token: {token}")

        return stack.to_list()
