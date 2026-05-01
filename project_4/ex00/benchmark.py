#!/usr/bin/env python3

import timeit

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

def get_gmails_loop(emails):
    result = []
    for email in emails:
        if email.endswith('@gmail.com'):
            result.append(email)
    return result

def get_gmails_listcomp(emails):
    return [email for email in emails if email.endswith('@gmail.com')]

if __name__ == '__main__':
    loop_time = timeit.timeit(lambda: get_gmails_loop(emails), number=900000)
    listcomp_time = timeit.timeit(lambda: get_gmails_listcomp(emails), number=900000)
    if listcomp_time <= loop_time:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')
    times = sorted([listcomp_time, loop_time])
    print(f"{times[0]} vs {times[1]}")
