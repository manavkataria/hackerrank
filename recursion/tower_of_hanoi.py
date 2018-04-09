#!/usr/bin/env python2

from __future__ import print_function

class Tower(object):
    def __init__(self, name, num_disks=0):
        self.name = name
        if num_disks != 0:
            self.content = range(num_disks, 0, -1)
        else:
            self.content = []

    def push(self, num):
        self.content.append(num)

    def pop(self):
        return self.content.pop()

    def __len__(self):
        return len(self.content)


def get_tower(towers, match_name):
    tw = filter(lambda x:x.name == match_name, towers)
    return tw[0]


def print_state(towers):
    a = get_tower(towers, 'A')
    b = get_tower(towers, 'B')
    c = get_tower(towers, 'C')

    print ('A:', a.content)
    print ('B:', b.content)
    print ('C:', c.content)
    print ()


def hanoi(n, frm, to, via):
    print_state([frm, to, via])

    if n == 1:
        print('Move:', frm.name, '->', to.name)
        to.push(frm.pop())
    else:
        hanoi(n-1, frm, via, to)
        hanoi(1, frm, to, via)
        hanoi(n-1, via, to, frm)

def steps_in_tower_of_hanoi(no_of_disks):
    a = Tower('A', no_of_disks)
    b = Tower('B')
    c = Tower('C')
    hanoi(no_of_disks, a, b, c)
    print_state([a, b, c])

    return [[0, 0, 0], [0, 0, 0]]


steps_in_tower_of_hanoi(3)
