#!/usr/bin/env python2

# Problem URL: https://www.hackerrank.com/contests/coding-test-1-bits-hyderabad/challenges/spiral-matrix-1/problem

# Extension: Do this for a non-square matrix

def spiral1d(matrix, sr, sc, count, rowdelta, coldelta):
    n = len(matrix)

    while(count > 0):
        print matrix[sr][sc],
        sr = sr + rowdelta
        sc = sc + coldelta
        count -= 1


def spiral2d(matrix):
    n = len(matrix)  # Assume Square

    for i in range(n/2):
        sr, sc = i, i
        spiral1d(matrix, sr, sc, n-2*i-1, rowdelta=0, coldelta=1)

        sr, sc = i, n-1-i
        spiral1d(matrix, sr, sc, n-2*i-1, rowdelta=1, coldelta=0)

        sr, sc = n-1-i, n-1-i
        spiral1d(matrix, sr, sc, n-2*i-1, rowdelta=0, coldelta=-1)

        sr, sc = n-1-i, i
        spiral1d(matrix, sr, sc, n-2*i-1, rowdelta=-1, coldelta=0)

    if n % 2 == 1:
        print matrix[n/2][n/2]

def main():
    n = input()

    matrix = []
    for i in range(n):
        matrix.append(raw_input().split())

    spiral2d(matrix)


if __name__ == '__main__':
    main()
