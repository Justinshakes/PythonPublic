import pytest
from numb3rs import validate


def test_valid_ips():
    assert validate("127.0.0.10") == True
    assert validate("255.255.255.0") == True


def test_invalid_letters_numbers():
    assert validate("1Dog2") == False
    assert validate("4Human6") == False


def test_invalid_ips_out_of_range():
    assert validate("275.3.6.28") == False
    assert validate("-1.3.6.28") == False
    assert validate("10.10.10.10.10") == False
    assert validate("20.3.6.999") == False
