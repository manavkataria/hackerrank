cache = dict()

def countBinTrees_memoized(n):
    if n < 0:
        return 0
    
    else:
        if n in cache:
            return cache[n]
        
        if 0 <= n <= 1:
            result = 1
        else:
            result = 0
            for i in range(n):
                result += countBinTrees_memoized(i)*countBinTrees_memoized(n-1-i)

        cache[n] = result
        return cache[n]


def countBinTrees_iterative(n):
    if n < 0:
        return 0
    else:
        cache = [1, 1]
        for i in range(2, n+1):
            cache.append(0)
            # print ('i:', i, 'Cache:', cache)
            for j in range(0, i):
                # print ('j:', j, 'i-j-1:', i-j-1)
                cache[i] += cache[j]*cache[i-j-1]
        
    return cache[n]

def countBinTrees_recursion(n):
    if n < 0:
        return 0
    
    if 0 <= n <= 1:
        return 1
    
    result = 0
    for i in range(n):
        result += countBinTrees_recursion(i)*countBinTrees_recursion(n-1-i)
    
    return result

def how_many_BSTs(n):
    if n == 0:
        return 0
    
    return countBinTrees_memoized(n)

