
def maxWinHelper(arr, i, j):
    """
    Return Pair(Best Max sum, Penultimate Best Max sum) for player given arr[i:j]

    TODO: Memoize
    """

    if i > j:
        return 0
    elif i == j:
        return arr[i]
    # else

    # Note: These are for the opponent
    # left  = maxWinHelper(arr, i+1, j)
    # right = maxWinHelper(arr, i, j-1)

    """
    current = max(leftSum, rightSum)
    Where
        leftSum = left + min(next-to-next-turn); Min coz the opponent gets the next best;
        rightSum = right + min(next-to-next-turn); Min coz the opponent gets the next best;
    """

    leftSum = arr[i] + min(maxWinHelper(arr, i+2, j),
                           maxWinHelper(arr, i+1, j-1))
    rightSum = arr[j] + min(maxWinHelper(arr, i+1, j-1),
                            maxWinHelper(arr, i, j-2))

    return max(leftSum, rightSum)

def maxWin(intCoins):
    i, j = 0, len(intCoins)-1
    p1 = maxWinHelper(intCoins, i, j)
    return p1
