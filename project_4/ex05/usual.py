#!/usr/bin/env python3

import sys
import resource

def read_all_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()

def get_cpu_time():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return usage.ru_utime + usage.ru_stime

def get_peak_memory():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python ordinary.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    start_cpu = get_cpu_time()
    start_mem = get_peak_memory()
    lines = read_all_lines(filename)

    for line in lines:
        pass
    
    end_cpu = get_cpu_time()
    end_mem = get_peak_memory()
    cpu_time = end_cpu - start_cpu
    peak_mem_kb = end_mem - start_mem
    peak_mem_gb = peak_mem_kb / (1024 * 1024)
    
    print(f"Peak Memory Usage = {peak_mem_gb:.3f} GB")
    print(f"User Mode Time + System Mode Time = {cpu_time:.2f}s")
