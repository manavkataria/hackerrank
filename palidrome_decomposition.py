#!/usr/bin/env python2


def ispalin(string):
    for i in range(len(string)/2):
        if not string[i] == string[-i-1]:
            return False
    return True


def palindec(s, results, pst, pend):
    pass


def palindec_deprecated(s, results, pst, pend):
    # Doesn't handle reusing a palindrome string. eg: 'aaaa' should yield 8 results
    # Guard
    if pend > len(s):
        return

    # Base
    if ispalin(s[pst:pend]):
        # print 'Palin?', s[pst:pend]
        # print 'pst(%d) pend(%d)' % (pst, pend)

        outstr = ''
        if pst > 0:
            outstr += '|'.join(s[:pst]) + '|'
        outstr += s[pst:pend]
        if pend < len(s):
            outstr += '|' + '|'.join(s[pend:])
        results.add(outstr)
    else:
        # Secondary Guard
        return

    # Transitions
    for pend in range(pst+2, len(s)+1):
        palindec_deprecated(s, results, pst+1, pend)

    return results


def generate_palindromic_decompositions(s):
    results = set()
    for end in range(1, len(s)+1):
        palindec_deprecated(s, results, 0, end)

    return results

result = generate_palindromic_decompositions('aaaa')
assert 8 == len(result), 'Result: ' + str(result)
