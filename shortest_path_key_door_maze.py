#!/usr/bin/env python2
# Shortest Path in 2D Grid with Keys and Doors

grid = ["+B...",
        "####.",
        "##b#.",
        "a...A",
        "##@##"
        ]

expected_output_len = 21

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

def get_neighbours(point, grid):
    lenx = len(grid)
    leny = len(grid[0])

    deltax = (1, -1, 0, 0)
    deltay = (0, 0, 1, -1)

    neighbours = list()
    for p in zip(deltax, deltay):
        newpt = point + Point(p[0], p[1])
        if (0 <= newpt.x < lenx and 0 <= newpt.y < leny):
            neighbours.append(newpt)

    return neighbours

def print_grid(grid, debugstr=None):
    print debugstr
    for row in grid:
        print row


def build_path(backpointer, start, end):
    # print_grid(backpointer, 'BackPointer:')
    path = [end]
    while (start != end):
        # print 'Path:', path
        # print 'End:', end
        bp = backpointer[end.x][end.y]
        path.append(bp)
        end = bp

    return path[::-1]


def bfs(grid, start, end):
    print '\nBFS:', start, '-->', end
    cache = [[cell for cell in row] for row in grid]
    backpointer = [['   ' for cell in row] for row in grid]
    q = [start]

    while len(q) > 0 and start != end:
        # print 'Queue:', q
        # print_grid(cache, 'Cache:')

        p = q.pop(0)
        cache[p.x][p.y] = 'v'
        for n in get_neighbours(p, grid):
            cell = cache[n.x][n.y]
            if cell != 'v' and cell != '#':
                backpointer[n.x][n.y] = p
                q.append(n)

    return build_path(backpointer, start, end)


def draw_path(grid, path_list, headstr='Global:'):
    path = {(p.x,p.y) for p in path_list}

    print headstr

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i,j) in path:
                print '*',
            else:
                print cell,
        print


def get_doors(grid, path):
    q = []
    for p in path:
        cell = grid[p.x][p.y]
        if cell.isupper():
            q.append((cell, p))
    return q


def shortest_path_to_key_and_door(grid, keys, key, start, doorpt):
    minpathlen = float('inf')
    minpath = None

    for keypt in keys[key]:
        path_to_key = bfs(grid, start, keypt)
        path_to_door = bfs(grid, path_to_key[-1], doorpt)
        path = path_to_key[:-1] + path_to_door  # Avoid Duplicate start and end in path

        if len(path) < minpathlen:
            minpathlen = len(path_to_key)
            minpath = path

    return minpath


def find_shortest_path(grid):
    keys = dict()
    doors = dict()
    start, end = None, None

    for x, row in enumerate(grid):
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

    # print 'Keys:', keys
    # print 'Doors:', doors
    print 'Start, End:', start, end

    path = bfs(grid, start, end)
    print 'Shortest Path:', path

    # Find relevant doors in shortest path:
    queue = get_doors(grid, path)
    print 'Encountered Doors:', queue

    print '\n### Key to Door (Rise and Repeat) ###'
    s = start
    global_path = []
    discovered_keys = set()
    for door, doorpt in queue:
        # Check whether you can get to the key or the door sooner.

        key = door.lower()
        if key not in discovered_keys:
            # Get Shortest Path to Key + Door
            print 'New Key!', key
            path = shortest_path_to_key_and_door(grid, keys, key, s, doorpt)
            print 'Key to Door:', path
            discovered_keys.add(door.lower())
        else:
            print 'Old Key!', key
            path = bfs(grid, s, doorpt)
            print 'Door to Door:', path

        global_path.extend(path[:-1])
        draw_path(grid, global_path)

        s = path[-1]  # Last Unlocked Door's Position
        print 'global_path:', global_path

    # Last Door to End
    last_path = bfs(grid, s, end)
    print 'Door to End:', last_path

    global_path += last_path
    draw_path(grid, global_path)

    minlen = len(global_path)
    print 'Final Global Path(%d): %s' %(minlen, (global_path))

    # outstr = '9' #  is the shortest length possible.  #% minlen
    # print outstr
    # with open(os.environ['OUTPUT_PATH'], 'w') as f:
    #     f.write(outstr)

    return []
