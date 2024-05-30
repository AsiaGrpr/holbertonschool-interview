#!/usr/bin/python3
"""
Minimum operation module
"""


def minOperations(n):
    """
    minOperations - Return the fewest number of operations needed
        to result of n H characters
    @n: The number of H characters needed - integer
    Return: The sum of the operations needed to attend n H - integer
            If n is impossible to achieve, return 0
    """
    if n <= 1:
        return 0

    num_operations = 0
    sum = 2

    while sum <= n:
        while n % sum == 0:
            num_operations += sum
            n //= sum
        sum += 1

    return num_operations
