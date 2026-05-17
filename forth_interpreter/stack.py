"""Stack abstraction used by the interpreter."""

from __future__ import annotations

from dataclasses import dataclass, field

from .errors import StackUnderflowError


@dataclass
class Stack:
    """Simple stack with explicit underflow checks."""

    _items: list[int] = field(default_factory=list)

    def push(self, value: int) -> None:
        self._items.append(value)

    def pop(self) -> int:
        if not self._items:
            raise StackUnderflowError("Cannot pop from an empty stack.")
        return self._items.pop()

    def peek(self, depth: int = 0) -> int:
        if depth < 0:
            raise ValueError("Stack depth cannot be negative.")
        if depth >= len(self._items):
            raise StackUnderflowError("Not enough values on the stack.")
        return self._items[-1 - depth]

    def require_depth(self, depth: int) -> None:
        if len(self._items) < depth:
            raise StackUnderflowError(
                f"Operation requires {depth} stack value(s), "
                f"but only {len(self._items)} available."
            )

    def to_list(self) -> list[int]:
        return list(self._items)

    def __len__(self) -> int:
        return len(self._items)
