def is_prime(n):
    """
    Checks if an integer, N is a prime number
    >>> is_prime(10)
    False
    >>> is_prime(5)
    True
    """
    assert n > 0, 'A positive integer is required'
    if n == 1: return False
    i = 2
    while n > i:
        if n % i == 0:
            return False
        i = i + 1
    return True