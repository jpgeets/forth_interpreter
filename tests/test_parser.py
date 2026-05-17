from forth_interpreter.parser import is_integer_token, parse_integer, tokenize


def test_tokenize_strips_extra_whitespace():
    assert tokenize("  3   4   +  ") == ["3", "4", "+"]


def test_tokenize_ignores_parenthesized_comments():
    assert tokenize("3 4 + ( add two numbers )") == ["3", "4", "+"]


def test_is_integer_token_accepts_negative_numbers():
    assert is_integer_token("-42")


def test_parse_integer_returns_int():
    assert parse_integer("42") == 42
