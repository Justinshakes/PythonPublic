from solution import problem


def test_problem1():
    assert problem("hello") == "Error"


def test_problem2():
    assert problem(1) == 56


if __name__ == "__main__":
    test_problem1()
    test_problem2()
