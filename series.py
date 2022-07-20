def fibonacci(n):
    """Delivers the nth element from a fibonacci sequence

    :param n: (int) defines the nth element to be requrests from the fibonacci sequence

    :return: (int) the value of the nth element of a fibonacci sequence
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Delivers the nth element from a lucas sequence

    :param n: (int) defines the nth element to be requrests from the lucase sequence

    :return: (int) the value of the nth element of a lucas sequence
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, first=0, second=1):
    """Delivers the nth element from a custom mathematical sequence

    :param n: (int) defines the nth element to be requrests from the custom mathematical sequence
    :param first: (int) defines the value of the first element of a custom mathematical sequence
    :param second: (int) defines the value of the second element of a custom mathematical sequence

    :return: (int) the value of the nth element of a custom mathematical sequence
    """
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)
