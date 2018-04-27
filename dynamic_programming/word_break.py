#!/usr/bin/env python2
# Dynamic Programming

def  wordBreak_bool(strWord, vocab):
    w = strWord

    M = [False]*(len(w)+1)
    M[-1] = True

    for i in range(len(w)-1, -1, -1):
        for v in vocab:
            # print 'i(%d) %s==%s' %(i, v, w[i:i+len(v)])
            if w[i:i+len(v)] == v:
                print 'Match Found!'
                if M[i+len(v)] == True:
                    M[i] = True
                    break
    print ' Final:', M
    return M[0]


def  wordBreak(strWord, vocab):
    w = strWord

    M = [[] for _ in range(len(w)+1)]
    M[len(w)] = [len(w)]  # Defines valid end-index (exclusive) that successfully break the full string starting at i as start index

    for i in range(len(w)-1, -1, -1):
        for v in vocab:
            # print 'i(%d) %s==%s' %(i, v, w[i:i+len(v)])
            # print 'M', M
            j = i+len(v)
            if w[i:j] == v:
                # print 'Match Found!'
                if len(M[j]) > 0:
                    M[i].append(j)
                    # break # NOTE: Don't break to find all valid successful terminations
    print 'Final:', M

    strings = []
    sofar = []
    current = 0
    dfs(w, current, M, strings, sofar)

    return strings

def dfs(w, current, M, strings, sofar):
    print 'current: %2d' % current, 'SoFar:', sofar

    if current == len(w):
        strings.append(' '.join(sofar))
        print 'Strings:', strings, '\n'
        return

    # Trim W and DFS
    for end in M[current]:
        dfs(w, end, M, strings, sofar + [w[current:end]])

strWord = 'catsanddog'
vocab = {'cats', 'cat', 'and', 'sand', 'dog'}

wordBreak(strWord, vocab)
