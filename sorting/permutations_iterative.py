#!/usr/bin/env python2

# Print all permutations of a String
# Eric Ho
# Company: Qventus
# 4th May 2018

def permutations(instr):
    partial = ['']

    for i, c in enumerate(instr):
        newlist = []

        while (len(partial) > 0):
            pstr = partial.pop()

            for k in range(len(pstr)+1):
                out = pstr[:k] + c + pstr[k:]

                newlist.append(out)

        partial = newlist

    print 'Output:', partial, len(partial)

instr = 'abcde'
permutations(instr)

"""
Approach:

[a]
[ab, ba]
[cab, acb, abc, cba, bca, bac]

24 + 6 + 2 + 1
O(Sigma-n)!)
"""
