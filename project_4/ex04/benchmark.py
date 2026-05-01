#!/usr/bin/env python3

import timeit
import random
from collections import Counter

numbers = [random.randint(0, 100) for i in range(1000000)]

def my_count(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    return counts

def my_top10(numbers):
    counts = my_count(numbers)
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]

def counter_count(numbers):
    return Counter(numbers)

def counter_top10(numbers):
    return Counter(numbers).most_common(10)

if __name__ == '__main__':
    t_my_count = timeit.timeit(lambda: my_count(numbers), number=1)
    print(f"my function: {t_my_count}")

    t_counter = timeit.timeit(lambda: counter_count(numbers), number=1)
    print(f"Counter: {t_counter}")

    t_my_top = timeit.timeit(lambda: my_top10(numbers), number=1)
    print(f"my top: {t_my_top}")

    t_counter_top = timeit.timeit(lambda: counter_top10(numbers), number=1)
    print(f"Counter's top: {t_counter_top}")
