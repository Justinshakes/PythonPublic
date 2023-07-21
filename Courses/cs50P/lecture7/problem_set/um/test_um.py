from um import count


def test_lower_and_upper_case():
    assert count("Um, thanks for the album.") == 1
    assert count("UM, thanks for the album.") == 1
    assert count("um, thanks for the album.") == 1


def test_multable_um():
    assert count("Um, thanks, um...") == 2
    assert count("Um, um, um...") == 3


def test_invalid():
    assert count("yummy") == 0
    assert count("rum") == 0

def test_unique_cases():
    assert count("um,") == 1
    assert count("um") == 1
    assert count("um?") == 1
    assert count("  um  ") == 1

