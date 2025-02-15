def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    if num < 10:
        if num == prev_digit:
            return 1
        else:
            return 0
    else:
        if num % 10 == prev_digit or num % 10 == (num % 100) // 10:
            return 1 + neighbor_digits(num // 10, num % 10)
        else:
            return neighbor_digits(num // 10, num % 10)

def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"
    
    if seq == 0:
        return True
    elif n == 0:
        return False
    else:
        if n % 10 == seq % 10:
            return has_subseq(n // 10, seq //10) or has_subseq(n // 10, seq)
        else:
            return has_subseq(n // 10, seq)