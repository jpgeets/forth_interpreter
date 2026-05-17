"""Small Forth-like interpreter package."""

from .errors import ForthError, InvalidNumberError, StackUnderflowError, UnknownTokenError
from .interpreter import Interpreter

__all__ = [
    "ForthError",
    "InvalidNumberError",
    "Interpreter",
    "StackUnderflowError",
    "UnknownTokenError",
]
