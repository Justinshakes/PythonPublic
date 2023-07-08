from plates import is_valid


def test_valid_plate():
    assert is_valid("CS50") == True


def test_invalid_digits_after_letters():
    assert is_valid("CS05") == False


def test_invalid_letters_after_digits():
    assert is_valid("CS50P") == False


def test_invalid_non_alphanumeric_characters():
    assert is_valid("PI3.14") == False


def test_invalid_single_letter():
    assert is_valid("H") == False


def test_invalid_more_than_4_characters():
    assert is_valid("OUTATIME") == False

def test_invalid_numbers_only():
    assert is_valid("123456") == False