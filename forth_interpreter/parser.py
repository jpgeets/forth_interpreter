"""Token parsing helpers."""

from __future__ import annotations

from .errors import InvalidNumberError


def strip_comments(code: str) -> str:
    """Remove simple parenthesized comments.

    Comments do not nest.
    """
    result: list[str] = []
    in_comment = False

    for char in code:
        if char == "(":
            in_comment = True
            continue
        if char == ")":
            in_comment = False
            continue
        if not in_comment:
            result.append(char)

    return "".join(result)


def tokenize(code: str) -> list[str]:
    """Split code into tokens after trimming whitespace and comments."""
    return strip_comments(code).strip().split()


def is_integer_token(token: str) -> bool:
    """Return True if token represents an integer token."""
    return token.isdigit()


def parse_integer(token: str) -> int:
    """Parse one integer token."""
    if not is_integer_token(token):
        raise InvalidNumberError(f"Invalid integer token: {token}")

    return token
