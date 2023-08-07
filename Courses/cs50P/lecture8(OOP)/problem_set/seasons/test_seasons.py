from seasons import check_birthday


def test_check_birthday():
    assert check_birthday("1998-07-03") == ("1998", "07", "03")
    assert check_birthday("1998-7-3") is None
    assert check_birthday("July 3, 1998") is None