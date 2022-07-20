from series import fibonacci, lucas, sum_series

# --------------------- Fibonacci Tests ---------------------


def test_fibo_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibo_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibo_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibo_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibo_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


# --------------------- Lucas Tests ---------------------


def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected


# --------------------- Sum Series tests ---------------------


def test_series_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_series_zero_three_three():
    actual = sum_series(0, 3, 3)
    expected = 3
    assert actual == expected


def test_series_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_series_one_three_three():
    actual = sum_series(1, 3, 3)
    expected = 3
    assert actual == expected


def test_series_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_series_two_three_three():
    actual = sum_series(2, 3, 3)
    expected = 6
    assert actual == expected


def test_series_three():
    actual = sum_series(3)
    expected = 2
    assert actual == expected


def test_series_three_three_three():
    actual = sum_series(3, 3, 3)
    expected = 9
    assert actual == expected


def test_series_four():
    actual = sum_series(4)
    expected = 3
    assert actual == expected


def test_series_four_three_three():
    actual = sum_series(4, 3, 3)
    expected = 15
    assert actual == expected
