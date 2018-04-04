#!/bin/env/python2.7
# Affirm Onsite
# See Collections.OrderedDict solution here: https://www.kunxi.org/blog/2014/05/lru-cache-in-python/

class Node(object):
    def __init__(self, key, data, prev=None, next=None):
        self.key = key
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        string = '{%d->%d}' % (self.key, self.data)
        return string


class Cache(object):

    def __init__(self):
        self.table = dict()  # Use: Collections.OrderedDict
        self.first = None
        self.last = None
        self.MAX = 5

    def get(self, key):
        print('\n[ACTION] LookUp:', key)
        if key in self.table:
            # TODO: Update First & Last
            node = self.table[key]

            if self.last == node:
                self.last = node.next
                self.last.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

            node.next = None
            node.prev = self.first
            self.first.next = node

            self.first = node

            return node
        else:
            return None

    def add_or_replace(self, key, data):
        if len(self.table) == 0:
            # First Node
            node = Node(key, data)
            self.first = node
            self.last = node
            self.table[key] = node
        elif 0 < len(self.table) < self.MAX:
            node = Node(key, data, prev=self.first, next=None) # might need a copy

            self.table[key] = node
            self.first.next = node

            self.first = node  # Ensure no self pointer
        else:
            # find oldest and replace pointers
            node = Node(key, data, prev=self.first, next=None)
            self.first.next = node
            self.first = node

            self.last.next.prev = None

            old_key = self.last.key
            del self.table[old_key]  # self.table.pop(old_key)
            self.table[key] = node

            self.last = self.last.next


    def __repr__(self):
        string = '\n--- CACHE ---'
        # string += '\nTable: ' + str(self.table)
        # string += '\nQueue:'
        string += '\nDescending:'
        node = self.first
        i = len(self.table)-1
        while node:
            string += '\n[%d] %d->%d' % (i, node.key, node.data)
            node = node.prev
            i -= 1

        string += '\nAscending:'
        node = self.last
        while node:
            i += 1
            string += '\n[%d] %d->%d' % (i, node.key, node.data)
            node = node.next
        # string += '\nLeast Recently Used: ' + str(self.last)
        return string


def main():
    """
    1. Add items till cache full
    2. if cache full replace lru item
    """
    # access = [1, 2, 3, 4, 5, 6]
    # data = [10, 20, 30, 40, 50, 60]

    access = [1, 2, 3, 4, 5, 1, 6]
    data = [10, 20, 30, 40, 50, -1, 60]

    cache = Cache()

    for i, key in enumerate(access):
        if not cache.get(key):
            cache.add_or_replace(key, data[i])

        print(cache)

if __name__ == '__main__':
    main()
