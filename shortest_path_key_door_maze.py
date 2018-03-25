#!/usr/bin/env python2
# Shortest Path in 2D Grid with Keys and Doors

grid = ["+B...",
        "####.",
        "##b#.",
        "a...A",
        "##@##"
        ]

expected_output_len = 17

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '[%d,%d]' % (self.x, self.y)

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Grid(object):
    def __init__(self, grid):
        self.grid = grid

    def get_neighbours(self, point):
        lenx = len(self.grid)
        leny = len(self.grid[0])

        deltax = (1, -1, 0, 0)
        deltay = (0, 0, 1, -1)

        neighbours = list()
        for p in zip(deltax, deltay):
            newpt = point + Point(p[0], p[1])
            if (0 <= newpt.x < lenx and 0 <= newpt.y < leny):
                neighbours.append(newpt)

        return neighbours

    def print_grid(self, debugstr=None):
        print debugstr
        for row in self.grid:
            print row

    def build_path(self, backpointer, start, end):
        # NOTE: Could be a @classmethod
        # print_grid(backpointer, 'BackPointer:')
        path = [end]
        while (start != end):
            # print 'Path:', path
            # print 'End:', end
            bp = backpointer[end.x][end.y]
            path.append(bp)
            end = bp

        return path[::-1]

    def bfs(self, start, end):
        print '\nBFS:', start, '-->', end
        cache = [[cell for cell in row] for row in self.grid]
        backpointer = [['   ' for cell in row] for row in self.grid]
        q = [start]

        while len(q) > 0 and start != end:
            # print 'Queue:', q
            # self.print_grid(cache, 'Cache:')

            p = q.pop(0)
            cache[p.x][p.y] = 'v'
            for n in self.get_neighbours(p):
                cell = cache[n.x][n.y]
                if cell != 'v' and cell != '#':
                    backpointer[n.x][n.y] = p
                    q.append(n)

        return self.build_path(backpointer, start, end)

    def draw_path(self, path_list, headstr='Global:'):
        path = {(p.x,p.y) for p in path_list}

        print headstr

        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if (i,j) in path:
                    print '*',
                else:
                    print cell,
            print

    def get_doors(self, path):
        """ Find Relevant Doors to path """

        # q = dict()
        q = list()
        for p in path:
            cell = self.grid[p.x][p.y]
            if cell.isupper():
                q.append((cell, p))
                # q[cell] = q.get(cell, []) + [p]
        return q

    def shortest_path_to_key_and_door(self, keys, key, start, doorpt):
        minpathlen = float('inf')
        minpath = None

        for keypt in keys[key]:
            path_to_key = self.bfs(start, keypt)
            path_to_door = self.bfs(path_to_key[-1], doorpt)
            path = path_to_key[:-1] + path_to_door  # Avoid Duplicate start and end in path

            if len(path) < minpathlen:
                minpathlen = len(path_to_key)
                minpath = path

        return minpath

    def sweep_for_keys_and_doors(self):
        keys = dict()
        doors = dict()
        start, end = None, None

        for x, row in enumerate(self.grid):
            for y, cell in enumerate(row):
                if cell == '@':
                    start = Point(x, y)
                elif cell == '+':
                    end = Point(x, y)
                elif cell.islower():
                    keys[cell] = keys.get(cell, []) + [Point(x,y)]
                elif cell.isupper():
                    doors[cell] = doors.get(cell, []) + [Point(x,y)]
                else:
                    assert cell == '.' or cell == '#' or cell == '\r', 'InvalidCell [%d,%d]: "%s(%d)" ' % (x, y, cell, ord(cell))
                    pass

        self.keys = keys
        self.doors = doors
        self.start = start
        self.end = end


def find_shortest_path(grid):
    maze = Grid(grid)
    maze.sweep_for_keys_and_doors()

    path = maze.bfs(maze.start, maze.end)
    print 'Shortest Path:', path

    # Find relevant doors in shortest path:
    queue = maze.get_doors(path)
    print 'Encountered Doors:', queue

    print '\n### Key to Door (Rise and Repeat) ###'
    s = maze.start
    global_path = list()
    discovered_keys = set()
    for door, doorpt in queue:
        # Check whether you can get to the key or the door sooner.

        key = door.lower()
        if key not in discovered_keys:
            # Get Shortest Path to Key + Door
            print 'New Key!', key
            path = maze.shortest_path_to_key_and_door(maze.keys, key, s, doorpt)
            print 'Key to Door:', path
            discovered_keys.add(door.lower())
        else:
            print 'Old Key!', key
            path = maze.bfs(s, doorpt)
            print 'Door to Door:', path

        global_path.extend(path[:-1])
        maze.draw_path(global_path)

        s = path[-1]  # Last Unlocked Door's Position
        print 'global_path:', global_path

    # Last Door to End
    last_path = maze.bfs(s, maze.end)
    print 'Door to End:', last_path

    global_path += last_path
    maze.draw_path(global_path)

    minlen = len(global_path)
    print 'Final Global Path(%d): %s' %(minlen, (global_path))

    return []

def main():
    if grid is not None:
        find_shortest_path(grid)
    else:
        pass
        # Define Grid for command line access


if __name__ == '__main__':
    main()
