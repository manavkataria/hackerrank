
# Dynamic Programming
# Robbery

"""
Source: http://codercareer.blogspot.com/2013/02/no-44-maximal-stolen-values.html
""""

def maxStolenValue(arrHouseValues):
    v = arrHouseValues
    M = [0]*(len(v)+1)

    for i in range(len(v), -1, -1):
        if i == len(v):
            value = 0
        elif i == len(v)-1:
            value = v[i]
        elif i == len(v)-2:
            value = max(v[i], v[i+1])
        else:
            value = max(v[i] + M[i+2], M[i])

        M[i] = value

    return M[0]

print maxStolenValue([6, 1, 2, 7])
