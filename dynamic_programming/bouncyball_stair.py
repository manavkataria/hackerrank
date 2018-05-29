#!/usr/bin/env python2

# Interviewer: Yuval Scharf
# Date: 27th May 2018

"""
Problem: Count the number of combinations that a bouncy ball takes to hit nth stair.
Constraint: Once it takes a bounce of size b, it has to take a bounce of size b or greater.

Test:

    n = 4 | Result = 5
    [
        [1, 1, 1, 1],
        [1, 1, 2],
        [1, 3],
        [2, 2],
        [4]
    ]

    n = 5 | Result = 7
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 2],
        [1, 2, 2],
        [1, 1, 3],
        [1, 4],
        [2, 3],
        [5]
    ]

"""


def print_table(table, caption=''):
    "Print Utility Function"
    print caption
    for i, row in enumerate(table):
        print str(i)+':', row


def bouncyball_stair(n, b):
    # NOTE: a base case of n == 1 is a trap!!
    if n == 0:
        return 1

    count = 0
    for i in range(b, n+1):
        count += bouncyball_stair(n-i, i)

    return count


memo = dict()
def bouncyball_stair_memo(n, b):
    if (n,b) not in memo:
        # NOTE: a base case of n == 1 is a trap!!
        if n == 0:
            memo[(n,b)] = 1
            return memo[(n,b)]

        count = 0
        for i in range(b, n+1):
            count += bouncyball_stair_memo(n-i, i)

        memo[(n,b)] = count
        return memo[(n,b)]
    else:
        return memo[(n,b)]


def bouncyball_stair_dpslow(N, b):
    """
    Memo -> DP:
    + Remove recursion;
    + Change `n` -> `N` in function(parameters)
    + Change `return` -> `continue`
    + Add 2D Bottom-up loops for DP:
        + NOTE: Go full length x full width, if basecase/initialization is inside ie;
        + Add n loop range(N)
        + Add b loop range(N)
    + Keep i-loop for computing each cell (already there)
    """

    for n in range(N+1):
        for b in range(1, N+1):

            # Base Case / Initialization
            if n == 0:
                memo[(n,b)] = 1
                continue

            count = 0
            for i in range(b, n+1):
                count += memo.get((n-i, i), 0)

            # Save
            memo[(n,b)] = count

    return memo[(N, 1)]


def bouncyball_dpfast_n3(N):
    """
    Use DP table to store number_of_stars and size_of_bounce: (N x B)
    For every cell, it takes O(N) lookups to compute its value.

    Time Complexity: O(N^3)
    Space Complexity: O(N^2)
    """
    table = [[0]*(N+1) for _ in range(N+1)]

    # Initialization: Needed outside
    for b in range(N+1):
        table[0][b] = 1

    for n in range(N+1):
        for b in range(1, n+1):
            for i in range(b,n+1):
                table[n][b] += table[n-i][i]

    return table[n][1]


def bouncyball_dpfast_n2(N):
    """
    Use additional space to save diagnoal sum and avoid recomputation
    For every cell, now it takes O(1) lookup to compute its value.

    Time Complexity: O(N^2)
    Space Complexity: O(2 * N^2)
    """

    # Additional Base for DP
    if N == 1:
        return 1

    # Save tuple: (Count-Value, Upperright Diagonal-Sum, _excluding itself_)
    table = [[(None, None)]*(N+1) for _ in range(N+1)]

    # Init the base case _outside_ (NOTE) the DP loops
    for b in range(1, N+1):
        table[0][b] = (1, 0)

    for n in range(1, N+1):

        # Run DP for the entire table range(N+1).
        # This is counter intuitive as the memoization->dp didn't need this, had range(n)
        # Also, n^3 solution also didn't need this.
        for b in range(1, N+1):

            # Add additional constraints for cv computation logic.
            # But keep that independent of DP loop range
            if b <= n:
                # count-value: upper-cv + upper-ds
                cv = table[n-b][b][0] + table[n-b][b][1]

                # Diagonal Sum; Additional constraint on b+1
                if b+1 <= N:
                    ds = table[n-1][b+1][0] + table[n-1][b+1][1]
                else:
                    ds = 1
            else:
                cv = 0
                ds = 1

            # Save Tuple
            table[n][b] = (cv, ds)

    return table[N][1][0]


def main():
    for i in range(1, 10):

        # result = bouncyball_stair(i, 1)  # Done
        # result = bouncyball_stair_memo(i, 1)  # Done
        # result = bouncyball_stair_dpslow(i, 1)  # Done
        # result = bouncyball_dpfast_n3(i)  # Done
        result = bouncyball_dpfast_n2(i)  # Done
        print 'N:', i, '| Count:', result


if __name__ == '__main__':
    main()
