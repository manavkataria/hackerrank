#!/usr/bin/env python2
# Problem: https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/

Dictionary = ['POON', 'SOON', 'NOON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN', 'SANE']

def isAdjacent(word1, word2):
    count = 0

    if len(word1) != len(word2):
        return False

    for i, j in zip(word1, word2):
        if i != j:
            count += 1

    return True if count == 1 else False

def word_ladder(start, end):
    q = list()
    q.append(start)
    count = 0

    # While q not empty
    while (len(q) > 0):
        root = q.pop(0)  # popleft() like a real FIFO queue
        print '\nDebug[%d]: Root: %s' % (count, root)
        print 'Debug[%d]: Queue: %s' % (count, q)

        if root == end:
            # print 'Debug: Path Found!'
            break

        # Add items to q if they are 1 distance away from root
        for word in Dictionary:
            # print '\nDebug: DictWord:', word
            if isAdjacent(word, root):
                print 'Debug: Adjacent Word:', word
                q.append(word)
                # Mark those items as visited
                Dictionary.remove(word)  # Might be invalid

        count += 1

    if root != end:
        return -1
        # Path Not Found
    else:
        return count

def main():

    test_params = [
        ('TOON', 'PLEA', 6),
        ('CATE', 'TANT', -1),
        ('SAME', 'SANE', 1),
        ]

    for start, end, steps in test_params:
        result = word_ladder(start, end)
        print '%s -[%d]-> %s; Found: %d' % (start, steps, end, result)
        assert result == steps

if __name__ == '__main__':
    main()
