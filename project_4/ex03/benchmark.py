#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

def sum_squares_loop(n):
    result = 0
    for i in range(1, n + 1):
        result += i * i
    return result

def sum_squares_reduce(n):
    return reduce(lambda s, x: s + x * x, range(1, n + 1), 0)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(0)

    func_name = sys.argv[1]
    try:
        number = int(sys.argv[2])
        n = int(sys.argv[3])
    except ValueError:
        print("Arguments must be integers")
        sys.exit(1)

    funcs = {
        'loop': lambda: sum_squares_loop(n),
        'reduce': lambda: sum_squares_reduce(n)
    }

    if func_name not in funcs:
        print("Unknown function name")
        sys.exit(1)

    t = timeit.timeit(funcs[func_name], number=number)
    print(t)
