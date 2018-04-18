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
    # Empty Target; Need two?
    # Empty Word
    # Empty words set
# 2. Dry Run
# 3. Use set instead of queue

# NOTE: Feedback
# Ask clarifying questions even thought the inputs are present; Do not assume that to be typical
# Possible to do target prefix lookup into words instead of for word in target
# DFS/BFS Revise
# Complexity analysis practice more

'''
T = len(target)
W = len(words)
n = len(max-len-word)

5 {a aa aaa aaaa aaaaa}
aaaaaab 7

7
'''


words = {'one', 'ca', 'cat', 'two', 'fo', 'four'}
target = 'onecat'

def find_concatenated_match(words, target):
    # Assume True; arbitrary choice
    if len(words) == 0:
        return True

    queue = [target]

    # 2 & 4 Repeat for all target candidates O(T)
    while len(queue) > 0:
        target = queue.pop()

        # 4 Repeat for one candidate O(T)
        while (target != ''):
            foundPrefix = False

            # 1 Prefix match every word O(W.n)
            for word in words:
                n = len(word)

                if n == 0:
                    return True

                print ('Target:', target, 'Word:', word)

                if word == target[:n]:
                    # 3 Trim Target
                    # target = target[n:]

                    # 2 Add back to queue; Multiple Matches
                    # queue.append(target)
                    queue.append(target[n:])
                    foundPrefix = True
                    # break

            # Try next target candidate; FIXME: Unnecessary?
            if foundPrefix == False:
                break
            else:
                # Found a prefix Match
                pass

        if target == '':
            break
            # Found Perfect Match
        else:
            pass
            # Try next candidate


    return foundPrefix


print find_concatenated_match(words, target)
