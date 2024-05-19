#!/usr/bin/python3
""""Trying to write a function that calculates minimum operationss"""

def min_operations(n):
    """"This function will find the minimum number of operations needed"""

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations


peter = min_operations(21)
print(peter)