#!/usr/bin/env python

import sys


def parse_input():
    N = int(sys.stdin.readline().strip())
    x = [int(i) for i in sys.stdin.readline().strip().split()]

    return N, x


def process_input(N, x):
    import ipdb; ipdb.set_trace()

    x_mean = 0
    for i in x:
        x_mean = x_mean + i
    x_mean = x_mean / N

    x_median = None
    x.sort()

    if N % 2 == 0:
        x_median = (x[int(N/2)-1] + x[int(N/2)])/2
    else:
        x_median = x[int(N/2)]

    return x_mean, x_median


def main():
    N, x = parse_input()
    x_mean, x_median = process_input(N, x)

    print(x_mean)
    print(x_median)


if __name__ == '__main__':
    main()
