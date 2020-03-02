#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Babatunde Odumosu"

import sys

def add(x, y):
    """Add two integers. Handles negative values."""
    # your code here
    return (x+y)


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    # your code here
    if y < 0:
        result = -multiply(x, -y)
    elif y == 0:
        result = 0
    elif y == 1:
        result = x
    else:
        result = x + multiply(x, y - 1)
    return(result)


def power(x, n):
    """Raise x to power n, where n >= 0"""
    # your code here
    total = x
    i = 1
    while i < n:
        x = multiply(total, x)
        i += 1
    return(x)

def factorial(x):
    """Compute factorial of x, where x > 0"""
    # your code here
    n = 1
    i = 1
    while i <= x:
        n = multiply(n, i)
        i += 1
    return(n)
    
def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    # your code here
    x = 0
    y = 1
    i = 0
    for i in range(n):
        x = y
        y = i
        i = add(x, y)
    return(i)
print(fibonacci(8))

def main():
    #if len(sys.argv) != 1:
        #print('usage: python main.py')
        #sys.exit(1)

        print(add(2, 4))
        print(multiply(6, -8))
        print(power(2, 8))
        print(factorial(4))
        print(fibonacci(8))

if __name__ == '__main__':
    # your code to call functions above
    main()