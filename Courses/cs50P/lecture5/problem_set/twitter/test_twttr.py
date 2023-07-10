from twttr import shorten


def test_shorten_word_with_vowels():
    assert shorten("Justin") == "Jstn"
    assert shorten("Hey Guys What's up") == "Hy Gys Wht's p"


def test_shorten_word_without_vowels():
    assert shorten("XYZ") == "XYZ"
    assert shorten("QWRTY") == "QWRTY"


def test_shorten_empty_string():
    assert shorten("") == ""


def test_shorten_word_with_only_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""


def test_shorten_word_with_only_non_vowels():
    assert shorten("BCDFG") == "BCDFG"
    assert shorten("bcdfg") == "bcdfg"


def test_shorten_word_with_repeated_characters():
    assert shorten("Mississippi") == "Msssspp"


def test_shorten_word_with_special_characters_and_spaces():
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("#Hashtag") == "#Hshtg"


def test_shorten_word_with_mixed_case():
    assert shorten("MiXeD") == "MXD"
    assert shorten("RaNdOm") == "RNdm"


def test_shorten_word_with_numbers():
    assert shorten("Abc123") == "bc123"
    assert shorten("Hello123World456") == "Hll123Wrld456"
