#!/usr/bin/env python2
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Hi! This is Manav.
"""
write a function max_collected_letters(input_str: str) -> int

'rbbwwbwbbrrr'
Return: 12

'rrbbrrbbbbrr'
Return: 8

1. Circular String
2. Collect consecutive sequnce of the same color
3. 'w' is a wildcard
4. Cut at every candidate and collect left and right. Return max for all i(left_i + right_i))

Approach 1:
Bruteforce: O(n*n)

TODO:
+ Approach2
+ Test Corner Cases
+ more..
"""

inputs = ['rrbbrrbbbbrr', 'rbbwwbwbbrrr']
expected = [8, 12]

def collect(input, pos, direction):
    """
        direction = 1 => right
        direction = -1 => left
        TODO: Consider Boolean
    """

    if len(input) == 0:
        return 0

    input = input[pos:] + input[:pos]
    if direction == -1:
        input = input[::-1]  # Reverse

    state = None
    c = input[0]

    if c == 'b' or c == 'r':
        state = c

    for i, c in enumerate(input):
        if state is None and c != 'w':
            state = c
        elif state is not None and c != state and c != 'w':
            break
        else:
            continue

    return i


def max_collected_letters(input):
    max = 0
    for i in range(len(input)):
        left = collect(input, i, -1)
        right = collect(input, i, 1)

        total = left+right
        if total > max:
            max = total
            print 'Max:', max, 'Split: %s %s' % (input[:i], input[i:])

    return max

for input, ex in zip(inputs, expected):
    print '\nInput:', input
    result = max_collected_letters(input)
    assert ex == result, '%d != %d' % (ex, result)
