#!/usr/bin/env python3

import timeit
import sys

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

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

def get_gmails_filter(emails):
    return list(filter(lambda email: email.endswith('@gmail.com'), emails))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(0)

    func_name = sys.argv[1]
    try:
        number = int(sys.argv[2])
    except ValueError:
        print("Second argument must be an integer")
        sys.exit(1)

    funcs = {
        'loop': lambda: get_gmails_loop(emails),
        'list_comprehension': lambda: get_gmails_listcomp(emails),
        'map': lambda: get_gmails_map(emails),
        'filter': lambda: get_gmails_filter(emails)
    }
    print(get_gmails_map(emails))

    if func_name not in funcs:
        print("Unknown function name")
        sys.exit(1)

    t = timeit.timeit(funcs[func_name], number=number)
    print(t)
