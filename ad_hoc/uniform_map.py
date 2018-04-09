#!/usr/bin/env python
# Uniform Distribution Map
# MagicMap

from random import randint


class UniformMap(object):
    def __init__(self):
        self.table = dict()
        self.array = []

    def __setitem__(self, k, v):
        m = len(self)
        self.table[k] = (v, m)
        self.array.append(k)

    def __len__(self):
        return len(self.array)

    def __getitem__(self, key=None):
        return self.table[key][0]

    def __delitem__(self, key):
        # 1. Get key from dict and delete
        v, i = self.table[key]
        del self.table[key]

        # 2. Swap k with last item in array and table

        m = len(self)
        k = self.array[m-1]
        if i != m-1:
            self.array[i] = k
            # Update Table Index
            self.table[k] = (self.table[k][0], i)

        # 3. Delete Last
        self.array.pop()

    def __iter__(self):
        # Helps avoid passing arguments to get on m like get m[5] implemented via self.__getitem__
        while True:
            m = len(self.array)
            if m > 0:
                i = randint(0, m-1)
                k = self.array[i]
                yield k, self.table[k][0]
            else:
                break

    def __repr__(self):
        return str(self.table)


def main():
    m = UniformMap()
    m['a'] = 'A'
    m['b'] = 'B'
    m['c'] = 'C'

    for i, j in enumerate(m):
        print ('GET:', j)
        if i == 6:
            break

    m['d'] = 'D'
    print ('\nAdding D')
    for i, j in enumerate(m):
        print ('GET:', j)
        if i == 10:
            break

    print('\nRandom Get + Delete:')
    for i, k in enumerate(m):
        del m[k[0]]
        print('Del[%s]: %s' % (k, m))


    print('\nRandom Adds')
    m['a'] = 'A'
    m['b'] = 'B'
    m['c'] = 'C'

    print('\nRandom Get + Delete:')
    for i, k in enumerate(m):
        del m[k[0]]
        print('Del[%s]: %s' % (k, m))

if __name__ == '__main__':
    main()
