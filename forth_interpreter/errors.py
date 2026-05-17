"""Custom exceptions for the Forth-like interpreter."""


class ForthError(Exception):
    """Base exception for interpreter errors."""


class StackUnderflowError(ForthError):
    """Raised when an operation needs more stack values than available."""


class UnknownTokenError(ForthError):
    """Raised when the interpreter receives an unknown token."""


class InvalidNumberError(ForthError):
    """Raised when a numeric token cannot be parsed as an integer."""
