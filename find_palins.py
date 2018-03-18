#!/usr/bin/env python2
# Enter your code here. Read input from STDIN. Print output to STDOUT

class Trie(object):
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children

    def __getitem__(self, i):
        return self.children.get(i, None) if self.children is not None else None

    def add(self, ch):
        if self.children is None:
            self.children = dict()
        trie_node = self.children.get(ch, Trie(ch))
        self.children[trie_node.value] = trie_node

    def __repr__(self):
        keys = self.children.keys() if self.children is not None else None
        return """Value: '%s' \t Children: %s""" % (self.value, keys)


def make_trie(words, suffix_tree=False):
    root = Trie('Root')

    for word in words:
        node = root
        print '\nProcessing:', word
        print '[Root]', root

        if suffix_tree: word = word[::-1]

        for c in word:
            node.add(c)  # Add if not exists; new node to previous node
            node = node[c]
            print '[New_]', node

        node.add('EOS')

    return root


def is_palin(word):
    # O(m)
    m = len(word)
    return word[:m/2] == word[m/2:m:-1]

def find_palins(words):
    root = make_trie(words, suffix_tree=True)

    for word in words:
        # O(N)
        node = root
        print '\nWord:', word
        import ipdb; ipdb.set_trace()

        for i, c in enumerate(word):
            print 'Char:', c

            if 'EOS' in node.children:
                if is_palin(word[i:]):
                    palindrome = word + word[:i][::-1]
                    print 'Palindrome:', palindrome

            node = node[c]
            if node is None:
                break

        if i == len(word)-1:
            # TODO: BFS -  Check all paths to understand whether the remaining trie letters form a palindrome

            if is_palin(remaining):
                palindrome = word + remaining[::-1]
                print 'Palindrome:', palindrome


def main():
    # words = read_input()
    words = set(['bat', 'stab', 'make'])
    print 'Words:', words
    palin_pairs = find_palins(words)

    write_output(palin_pairs)


def read_input():
    from sys import stdin
    words = set()
    for word in stdin:
        word = word.strip()
        # print 'Word:', word
        words.add(word)
    return words


def write_output(res):
    import os
    outfile = os.environ.get('OUTPUT_PATH', None)

    print '\nGenerating Output:'

    if outfile is not None:
        f = open(outfile, 'w')
        f.write(str(res))
        f.close()
    else:
        print str(res)


if __name__ == '__main__':
    main()
