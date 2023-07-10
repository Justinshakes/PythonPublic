from plates import is_valid


def test_valid_plate():
    assert is_valid("CS50") == True


def test_invalid_first_num_is_0():
    assert is_valid("CS05") == False


def test_invalid_non_alphanumeric_characters():
    assert is_valid("PI3.14") == False


def test_invalid_single_letter():
    assert is_valid("H") == False


def test_invalid_numbers_only():
    assert  is_valid("123456") == False

