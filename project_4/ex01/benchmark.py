#!/usr/bin/env python3

import timeit

emails = [
    'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'
] * 5

def get_gmails_loop(emails):
    result = []
    for email in emails:
        if email.endswith('@gmail.com'):
            result.append(email)
    return result

def get_gmails_listcomp(emails):
    return [email for email in emails if email.endswith('@gmail.com')]

def get_gmails_map(emails):
    return list(map(lambda email: email if email.endswith('@gmail.com') else None, emails))

if __name__ == '__main__':
    loop_time = timeit.timeit(lambda: get_gmails_loop(emails), number=900000)
    listcomp_time = timeit.timeit(lambda: get_gmails_listcomp(emails), number=900000)
    map_time = timeit.timeit(lambda: get_gmails_map(emails), number=900000)
    min_time = min(loop_time, listcomp_time, map_time)
    if min_time == map_time:
        print('it is better to use a map')
    elif min_time == listcomp_time:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')
    times = sorted([map_time, listcomp_time, loop_time])
    print(f"{times[0]} vs {times[1]} vs {times[2]}")
