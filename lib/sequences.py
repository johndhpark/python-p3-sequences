#!/usr/bin/env python3

def print_fibonacci(length):
    result = []

    for idx in range(0, length):
        if idx == 0 or idx == 1:
            result.append(idx)
        else:
            result.append(result[idx - 1] + result[idx - 2])

    print(result)
    