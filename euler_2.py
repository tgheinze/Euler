__author__ = 'tgheinze'

import sys
from pprint import pprint as pp


max = 4000000

def fib(m):
    t = 0
    a, b = 0, 1
    while b < m:
        if not(b%2):
            # print b
            t += b
        # print (b)
        a, b = b, a+b

    return t


print fib(max)
