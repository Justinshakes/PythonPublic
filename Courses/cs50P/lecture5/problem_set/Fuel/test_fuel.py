import pytest

from fuel import convert, gauge


def test_valid():
    assert convert("1/2") == 50 and gauge(convert("1/2")) == "50%"
    assert convert("1/100") == 1 and gauge(convert("1/100")) == "E"
    assert convert("99/100") == 99 and gauge(convert("99/100")) == "F"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("Dog")
