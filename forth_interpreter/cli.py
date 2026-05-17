"""Command-line interface for the Forth-like interpreter."""

from __future__ import annotations

import argparse

from .errors import ForthError
from .interpreter import Interpreter


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a small Forth-like interpreter.")
    parser.add_argument("code", nargs="+", help="Code to execute, e.g. '3 4 +'")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    code = " ".join(args.code)
    interpreter = Interpreter()

    try:
        print(interpreter.execute(code))
    except ForthError as error:
        print(f"Error: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
