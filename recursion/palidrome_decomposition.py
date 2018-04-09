#!/usr/bin/env python2


def ispalin(string):
    for i in range(len(string)/2):
        if not string[i] == string[-i-1]:
            return False
    return True


def palindec_results_returned(s, sofar, pst, pend):
    # Guard
    palinstr = s[pst:pend]
    if not ispalin(palinstr):
        return []

    # NOTE: PreTransition & also PreBase
    if len(sofar) == 0:
        sofar = palinstr
    else:
        sofar = sofar + '|' + palinstr

    # Base
    if pend == len(s):
        return [sofar]

    # Transitions
    results = []
    for tail in range(pend+1, len(s)+1):
        results += palindec_results_returned(s, sofar, pend, tail)

    return results

def palindec_structured(s, results, sofar, pst, pend):
    # Guard
    palinstr = s[pst:pend]
    if not ispalin(palinstr):
        return

    # NOTE: PreTransition & also PreBase
    if len(sofar) == 0:
        sofar = palinstr
    else:
        sofar = sofar + '|' + palinstr

    # Base
    if pend == len(s):
        results.add(sofar)
        return

    # Transitions
    for tail in range(pend+1, len(s)+1):
        palindec_structured(s, results, sofar, pend, tail)

    return results


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
    results = []
    sofar = ''

    for end in range(1, len(s)+1):
        # palindec_deprecated(s, results, 0, end)
        # palindec_structured(s, results, sofar, 0, end)
        results += palindec_results_returned(s, sofar, 0, end)

    return results

# result = generate_palindromic_decompositions('eeeeeeeeeeeeeeeeeeee')  # len: 524288
result = generate_palindromic_decompositions('aaaa') # 'aa|aa' unaccounted in deprecated_solution

outstr = 'Result[%d]: %s' % (len(result), str(result)[:100])
print outstr
assert 8 == len(result), outstr
