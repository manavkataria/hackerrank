#!/usr/bin/env python2

'''

Given a set of strings, e.g. {'one', 'cat', 'two', 'four'}, and a target string, e.g.
'fouroneone', return true if the target string is composed (by concatenation) of elements
from the set.

'fouroneone' -> true
'onecat' -> true
'fouron' -> false
'twone' -> false

'''

# NOTE: Approach
# 1 Prefix match every word
# 2 Keep track of multiple matches
# 3 Trim target with prefix and build new target; (Add to queue?)
# 4 Repeat

# TODO:
# 1. Corner / Edge Cases
    # Empty Target
    # Empty Word
    # Empty words set
# 2. Dry Run (done)
# 3. Use set instead of queue (done)

# NOTE: Feedback
# Ask clarifying questions even thought the inputs are present; Do not assume that to be typical
# Possible to do target prefix lookup into words instead of looking up each word in target
# DFS/BFS Revise
# Complexity analysis practice more

'''
Degenerate Case:
    5 {a aa aaa aaaa aaaaa}
    aaaaaab 7
'''


words = {'one', 'ca', 'cat', 'two', 'fo', 'four'}
targets = ['onecat', 'fouroneone', 'fouron', 'twone', '']
expected = [True, True, False, False, False]

def find_concatenated_match(words, target):
    """
        Time Complexity: O(T.W.n)
        T = len(target)
        W = len(words)
        n = len(max-wordlen)

        Space Complexity: O(W)
    """

    # Assume True; arbitrary choice
    if len(words) == 0:
        return True

    queue = set([target])

    # 2 & 4 Repeat for all target candidates O(T)
    while len(queue) > 0:
        target = queue.pop()

        # 1 Prefix match every word O(W.n)
        for word in words:
            n = len(word)

            if n == 0:
                return True

            print ('Target:', target, 'Word:', word)

            if word == target[:n]:
                # 3 Trim Target, and
                # 2 Add back to queue; Multiple Matches
                queue.add(target[n:])

                # Check for perfect match
                if target[n:] == '':
                    return True

    return False


def main():
    for target, expect in zip(targets, expected):
        found = find_concatenated_match(words, target)
        print 'Target:', target, '| Found:', found, '\n'
        assert found == expect


if __name__ == '__main__':
    main()
