#!/usr/bin/env python2

from __future__ import print_function

import os
import sys
## Boilerplate (above)

delta = (
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2)
)

inf = float ('inf')

def recHelper(graph, cur, end):
    rows = len(graph)
    cols = len(graph[0])

    if not (0 <= cur[0] < rows and 0 <= cur[1] < cols):
        return inf

    # Check if Visited; if yes, return plen, otherwise mark as visited and continue
    if graph[cur[0]][cur[1]][0] == 'v':
        return graph[cur[0]][cur[1]][1]
    else:
        graph[cur[0]][cur[1]] = ('v', graph[cur[0]][cur[1]][1])

    if cur == end:
        return 0

    pathlen = 0
    minpathlen = inf
    for d in delta:
        node = (cur[0] + d[0], cur[1] + d[1])
        pathlen = recHelper(graph, node, end)
        if pathlen != inf:
            graph[node[0]][node[1]] = (graph[node[0]][node[1]][0], pathlen)

        if pathlen < minpathlen:
            minpathlen = pathlen

    # print('\nCur:', cur, 'Pathlen:', minpathlen)
    # print('Graph:')
    # for row in graph:
    #     print(row)

    return 1 + minpathlen

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    graph = [[(' ', inf) for _ in range(cols)] for _ in range(rows)]
    plen = 0
    cur = (start_row, start_col)
    end = (end_row, end_col)

    graph[cur[0]][cur[1]] = ('s', inf)
    graph[end[0]][end[1]] = ('e', inf)

    val = recHelper(graph, cur, end)
    return val if val != inf else -1

## Boilerplate
os.environ['OUTPUT_PATH'] = '/dev/stdout'
sys.setrecursionlimit(50000)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    rows = int(raw_input())
    cols = int(raw_input())
    start_row = int(raw_input())
    start_col = int(raw_input())
    end_row = int(raw_input())
    end_col = int(raw_input())

    res = find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col)

    f.write(str(res) + "\n")
    f.close()
