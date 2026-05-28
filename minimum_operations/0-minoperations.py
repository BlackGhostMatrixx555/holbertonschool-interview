#!/usr/bin/python3
"""Module that calculates the minimum number of operations to reach n H's."""


def minOperations(n):
    """Calculate the fewest operations to result in exactly n H characters.

    Uses prime factorization: to reach n chars, you multiply by prime factors.
    Each prime factor p costs p operations (1 Copy All + p-1 Pastes).

    Args:
        n (int): the target number of H characters.

    Returns:
        int: minimum number of operations, or 0 if impossible.
    """
    if n <= 1:
        return 0
    ops = 0
    factor = 2
    while factor <= n:
        while n % factor == 0:
            ops += factor
            n //= factor
        factor += 1
    return ops
