#!/usr/bin/env python2


def explore_all_neighbors(z, i, visited, count):
    """
    Visits all neighbours and marks them as visited (resets) their connection
    Returns: Boolean if atleast 1 neighbour found apart from self
    """

    n = len(z)
    q = [i]
    found = set()
    while len(q) > 0:
        i = q.pop()

        for j in range(n):

            if z[i][j] == 1:  # Reset All Neighbours
                z[i][j] = 0
                z[j][i] = 0
                found.add(j)
                q.append(j)

    return found


def zombieCluster(zombies):
    n = len(zombies)
    z = [[1 if v == '1' else 0 for v in row] for row in zombies]

    # print 'Z', z
    count = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            found = explore_all_neighbors(z, i, visited, count)
            visited = visited.union(found)
            count += 1

    return count


def main():
    inputs =[['1100',
              '1110',
              '0110',
              '0001'],
             ['1000',
              '0100',
              '0010',
              '0001']]

    components = [2, 4]

    for graph, component in zip(inputs, components):
        result = zombieCluster(graph)
        assert result == component, 'Result: %s != %s' % (result, component)


if __name__ == '__main__':
    main()
