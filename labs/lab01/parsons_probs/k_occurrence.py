def k_occurrence(k, num):
    """
    >>> k_occurrence(5, 10)  # .Case 1
    0
    >>> k_occurrence(5, 5115)  # .Case 2
    2
    >>> k_occurrence(0, 100)  # .Case 3
    2
    >>> k_occurrence(0, 0)  # .Case 4
    0
    """
    "*** YOUR CODE HERE ***"
    if num == 0:
        return 0
    count = 0
    while num > 0:
        remain = num % 10
        num = num//10
        if remain == k:
            count += 1
    return count
