#!/usr/bin/env python2

def makeChange(C, intDenominations):
    D = intDenominations
    inf = float('inf')
    M = [inf]*(C+1)
    M[0] = 0  # NOTE: Helps with dfs find_min at the last step

    for i in range(1, C+1):  # NOTE: Important to start from 1; Don't overwrite M[0]
        min = inf
        for j in D:
            if i == j:
                min = 1
                break
            else:
                if (i-j)>=0 and M[i-j] < min:
                    min = M[i-j]+1
        M[i] = min

    print 'Final M:'
    print M
    result = []
    sofar = []
    dfs(C, intDenominations, M, result, sofar)
    print 'Result:', result

    resultset = set()
    for lst in result:
        freq = {d:0 for d in D}
        for d in lst:
            freq[d] += 1
        freq_tup = tuple((d,count) for d,count in freq.items())
        print freq
        resultset.add(freq_tup)

    print resultset
    return resultset

def dfs(C, D, M, result, sofar):
    if C < 0:
        return

    if C == 0:
        result.append(sofar)
        return

    # Find All Minidx
    min = float('inf')
    minidx = []
    for d in D:
        nextIdx = C-d
        if nextIdx < 0:  # NOTE: if these values are negavite, list can wrap around. Caution!
            continue
        if M[nextIdx] < min:
            min = M[nextIdx]
            minidx = [nextIdx]
        elif M[nextIdx] == min:
            minidx.append(nextIdx)

    print 'MinIdx:', minidx
    for idx in minidx:
        d = C-idx
        print 'd:', d, 'sofar:', sofar
        dfs(idx, D, M, result, sofar + [d])


makeChange(7, [1,2,3])
