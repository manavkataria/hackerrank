#!/usr/bin/env python2

# Dynamic Programming

def debug(M, title=''):
    print (title)
    for row in M:
        print (row)

def find_if_strings_interleave(A, B, I):
    """
    returns True if I[i+j:] interleaves A[i:] abd B[j:]

    This Needs DP not just a simple linear loop. Because, if the strings have overlapping character set, you won't know which string A or B to chose to increment. Hence you need backtracking, which can be optimized using DP
    """
    l = len(I)
    n = len(A)
    m = len(B)

    M = [[False]*(m+1) for _ in range(n+1)]

    if m+n == l:
        if l == 0:
            return True
        else:
            M[n][m] = True
    else:
        return False

    for i in range(n, -1, -1):
        for j in range(m, -1, -1):
            debug(M, 'Loop: %d, %d' % (i,j))

            if i<n and I[i+j] == A[i]:
                M[i][j] = M[i+1][j]
            elif j<m and I[i+j] == B[j]:
                M[i][j] = M[i][j+1]
            else:
                M[i][j] = True if i==n and j==m else False

    return M[0][0]
