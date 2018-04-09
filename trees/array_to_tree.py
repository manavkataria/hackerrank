#!/usr/bin/env python2

N = 9  # Number of Nodes in Tree

class Node(object):
    def __init__(self, val=-1, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        # print 'New Node: ', self.val

    @classmethod
    def inorder(cls, root):
        if root is None:
            return

        for val in cls.inorder(root.left):
            yield val

        yield root.val

        for val in cls.inorder(root.right):
            yield val

    @classmethod
    def print_inorder(cls, root):
        print 'Inorder: ',
        for val in cls.inorder(root):
            print val,


def build_balanced_bst(array):
    print 'Array:', array

    n = len(array)
    if n == 0:
        return

    root = Node(array[n/2])
    root.left = build_balanced_bst(array[:n/2])
    root.right = build_balanced_bst(array[n/2 + 1:])
    return root


def main():
    array = list(range(1, N+1))  # Sorted Array
    root = build_balanced_bst(array)
    Node.print_inorder(root)


if __name__ == '__main__':
    main()
