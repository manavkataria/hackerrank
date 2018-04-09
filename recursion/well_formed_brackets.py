#!/usr/bin/env python2

expected = [
    '((()))',
    '(()())',
    '(())()',
    '()(())',
    '()()()'
]

def wellformed(left, right=None):
    # Guard
    if left < 0:
        return

    if right is None:
        right = left

    # Base
    if left == right == 0:
        yield ""

    # Transitions
    # if left > 0:
    for parenstr in wellformed(left-1, right):
        print left-1, right, "(" + parenstr
        yield "(" + parenstr

    if right > left:
        for parenstr in wellformed(left, right-1):
            print left, right-1, ")" + parenstr
            yield ")" + parenstr



result = wellformed(2)
print list(result)
# assert set(expected) == set(result)
