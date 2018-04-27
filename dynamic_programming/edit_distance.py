#!/usr/bin/env python2
# Dynamic Programming
# 60mins
# Edit Distance

def levenshteinDistance(strWord1, strWord2):
    s = strWord1
    p = strWord2

    # Initialize Memory
    M = [[0]*(len(p)+1) for _ in range(len(s)+1)]

    for i in range(len(s), -1, -1):
        for j in range(len(p), -1, -1):
            if i == len(s):
                M[i][j] = len(p) - j
            elif j == len(p):
                M[i][j] = len(s) - i
            elif s[i] == p[j]:
                M[i][j] = M[i+1][j+1]
            else:
                M[i][j] = min(M[i+1][j+1], M[i+1][j], M[i][j+1]) + 1

    print 'Final M'
    for i in range(len(M)):
        print M[i]

    return M[0][0]

ss = ['cat', 'pizza', 'kitten']
pp = ['bat', 'yolo', 'sitting']
expected = [1,5,3]

for s, p, e in zip(ss, pp, expected):
    print '\nInput:', s, '->', p
    assert e == levenshteinDistance(s, p)
