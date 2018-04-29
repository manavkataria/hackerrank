def countWaysToClimb_recursion(steps, n):
    if n < 0:
        return 0

    if n == 0:
        return 1

    count = 0
    for s in steps:
        count += countWaysToClimb_recursion(steps, n-s)

    return count


def countWaysToClimb(steps, n):
    print ('Steps:', steps)
    print ('N:', n)

    M = [0]*(n+1)
    for i in range(1, n+1):
        for s in steps:
            if s == i:
                M[i] += 1
            else:
                M[i] += M[i-s] if (i-s)>0 else 0

    print(M)
    return M[n]
