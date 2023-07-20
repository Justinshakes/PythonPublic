from working import convert
import pytest


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("1 AM too 3 PM")


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 AM - 18 PM")


def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9:70 AM - 9:60 PM")


def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

