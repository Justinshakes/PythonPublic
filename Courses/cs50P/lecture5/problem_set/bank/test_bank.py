from bank import value
import pytest


def test_no_spaces():
    assert value("hello") == "$0"


def test_with_spaces():
    assert value("Hello Newman") == "$0"


def test_with_punctuation_and_spaces():
    assert value("Hello, Newman") == "$0"
    assert value("How you doing?") == "$20"
    assert value("What's happening?") == "$100"


if __name__ == "__main__":
    test_no_spaces()
    test_with_spaces()
    test_with_punctuation_and_spaces()