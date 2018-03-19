#!/usr/bin/env python2
from __future__ import print_function


"""
TestCase:
10000
10
9876
8
1234
2

Expected Output:
4322
"""

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

def knights_tour_recursive(graph, cur, end):
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
        pathlen = knights_tour_recursive(graph, node, end)
        if pathlen != inf:
            graph[node[0]][node[1]] = (graph[node[0]][node[1]][0], pathlen)

        if pathlen < minpathlen:
            minpathlen = pathlen

    # print('\nCur:', cur, 'Pathlen:', minpathlen)
    # print('Graph:')
    # for row in graph:
    #     print(row)

    return 1 + minpathlen

def knights_tour_iterative(graph, cur, end, start=None):
    """
    NOTE: This is a BFS solution. Hence it looks a little different from
    a DP up solution which is a reverse DFS approach.
    """
    rows = len(graph)
    cols = len(graph[0])

    graph[end[0]][end[1]] = ('e', 0)  # Initialized End Val
    queue = [end]  # Queue Inited
    cur = end

    while queue:
        cur = queue.pop(0)
        # print('\nCur:', cur)
        # print('Queue:', queue)
        # print('Graph:')
        # for row in graph:
        #     print(row)

        graph[cur[0]][cur[1]] = ('v', graph[cur[0]][cur[1]][1])

        pathlen = inf
        for d in delta:
            node = (cur[0] + d[0], cur[1] + d[1])
            pathlen = 1 + graph[cur[0]][cur[1]][1]

            if pathlen != inf and (0 <= node[0] < rows and 0 <= node[1] < cols) and graph[node[0]][node[1]][0] != 'v':
                graph[node[0]][node[1]] = ('v', pathlen)

                queue.append(node)

            # Term Condition
            if node == start:
                break

    return graph[start[0]][start[1]][1]


def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    graph = [[(' ', inf) for _ in range(cols)] for _ in range(rows)]
    plen = 0
    cur = (start_row, start_col)
    end = (end_row, end_col)

    graph[cur[0]][cur[1]] = ('s', inf)
    graph[end[0]][end[1]] = ('e', inf)

    # val = knights_tour_recursive(graph, cur, end)
    val = knights_tour_iterative(graph, cur, end, (start_row, start_col))
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
