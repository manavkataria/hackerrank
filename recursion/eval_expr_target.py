#!/usr/bin/env python2

# Generate all expressions that evaluate to target

import re
operator_matcher = re.compile('(\+|\*)')

def evaluate(expr):
    # Eliminate leading zeros that incorrectly cast decimal to octal (given the context of this problem)
    # Regex Reference: https://stackoverflow.com/a/9843145/1321129
    return eval(re.sub(r'\b0+(?!\b)', '', expr))


def evaluate_slow(expr):
    exp = operator_matcher.split(expr)

    for i, val in enumerate(exp):
        if val != '+' and val != '*':
            exp[i] = str(int(val))

    return eval(''.join(exp))


def evalexpr(s, l, target):
    if len(l) == 0:
        # Base
        if evaluate(s) == target:
            return [s]
        else:
            return []

    # Else
    results = []
    results += evalexpr(s + ''  + l[0], l[1:], target)
    results += evalexpr(s + '+' + l[0], l[1:], target)
    results += evalexpr(s + '*' + l[0], l[1:], target)

    return results

def generate_all_expressions(s, target):
    if len(s) > 0:
        return evalexpr(s[0], s[1:], target)
    else:
        return []

print generate_all_expressions('0123456789012', 123456789012)
print generate_all_expressions('9909059799853', 764)
