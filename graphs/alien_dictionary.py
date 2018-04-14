#!/usr/bin/env python2
# Alien Dictionary


class Graph(object):
    def __init__(self):
        self.innodes = dict()
        self.outnodes = dict()

    def add_dep(self, n1, n2):
        self.innodes[n1] = self.innodes.get(n1, set())   # Get/Create Empty Node for N1
        self.innodes[n2] = self.innodes.get(n2, set())   # Get/Create Empty Node for N2
        self.innodes[n2].add(n1)

        self.outnodes[n1] = self.outnodes.get(n1, set())  # Get/Create Empty Node for N1
        self.outnodes[n2] = self.outnodes.get(n2, set())  # Get/Create Empty Node for N2
        self.outnodes[n1].add(n2)

    def del_dep(self, n):
        values = self.outnodes[n]
        # print('Del Dependency Start:\nInNodes:', self.innodes, '\nOutNodes:' , self.outnodes)

        for v in values:
            self.innodes[v].remove(n)

        del self.innodes[n]
        del self.outnodes[n]

        # print('Del Dependency End:\nInNodes:', self.innodes, '\nOutNodes:' , self.outnodes)

    def find_zero_indegree(self):
        # print('Find Zero InDeg:')
        for k, v in self.innodes.items():
            # print('Checking:', k, ':', v)
            if len(v) == 0:
                return k

        return None

    def top_sort(self):
        alphabet = []
        while (len(self.innodes.keys()) != 0):
            key = self.find_zero_indegree()
            print('\nZero InDeg:', key)
            if key is not None:
                self.del_dep(key)
                alphabet.append(key)
            else:
                break
            print('Graph TopSort:\nInNodes:', self.innodes, '\nOutNodes:' , self.outnodes)
            print('Alphabet:', alphabet)

        return alphabet

def find_first_diff_char(str1, str2):
    m = min(len(str1), len(str2))
    i = 0
    while i < m:
        if str1[i] != str2[i]:
            return (str1[i], str2[i])
        i += 1

    return None, None


def find_order(words):
    graph = Graph()

    # Corner Case: If only one word in dict
    if len(set(words)) == 1:
        return words[0][0]

    prev = words[0].strip()
    for i, word in enumerate(words[1:], start=1):
        word = word.strip()

        print('\n[%d] %s ~ %s' % (i, prev, word))
        c1, c2 = find_first_diff_char(prev, word)

        if c1 is not None:
            print('Add Dep:', c1, '->', c2)
            graph.add_dep(c1, c2)
        else:
            # Corner Case: ['i', 'id'] but d -> i
            pass

        prev = word

        print('Graph WIP:\nInNodes:', graph.innodes, '\nOutNodes:' , graph.outnodes)

    print('\nGraph Ready:\nInNodes:', graph.innodes, '\nOutNodes:' , graph.outnodes)

    alphabet = graph.top_sort()

    return ''.join(alphabet)
