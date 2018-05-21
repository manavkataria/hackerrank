#!/usr/bin/env python2

"""
Minimum Window Substring
    S = 'ABAZA'
    T = 'AAZ'
    output = 'AZA'
"""

def  MinWindow(strText, strCharacters):
    S = strText
    T = strCharacters  # Pattern

    n = len(S)
    m = len(T)

    t = {}
    d = {}
    for c in T:
        t[c] = 0
        d[c] = d.get(c, 0) + 1  # Desired

    numSet = 0
    expand = True

    min = float('inf')
    mini = -1
    minj = -1

    i = 0
    j = -1

    while i < n:
        # Check AllSet?
        if numSet == m:
            expand = False

            # Check Min
            if j-i+1 < min:
                mini = i
                minj = j+1
                min = j-i+1

        if expand:
            # Bounds Check
            if j+1 < n:
                j+=1

                # Do Expansion
                c = S[j]
                if c not in t:
                    continue  # Ignore Char

                if t[c] < d[c]:
                    numSet += 1
                else:
                    # Repeats; No New Sets
                    pass

                t[c] += 1

            else:
                expand = False
                continue
        else:
            # contract

            # Bounds Check
            if i < n:
                c = S[i]

                if c not in t:
                    i+=1
                    continue

                # Do Contraction
                if t[c] == d[c]:
                    numSet -= 1

                    # Check AllSet?
                    if numSet < m:
                        expand = True

                t[c] -=1
                i+=1

    if min <= len(S):
        return S[mini:minj]
    else:
        return ''


# print MinWindow('A1BA', 'AB')
# print MinWindow('caaec', 'ace')
# print MinWindow('aab', 'aab')
print MinWindow('acdbddddddddaaaaaaaadabbbba', 'baad')
