#!/usr/bin/env python2

from random import randint

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

initialized = [
    [1, 8, 8, 1],
    [4, 8, 5, 1],
    [8, 4, 5, 4],
    [8, 1, 9, 8]
]

# initialized = [
#     [1, 2],
#     [3, 4]
# ]

class Grid(object):

    def __init__(self, cols=None, rows=None, values_max=9, initialize_with=None, copy_from=None):
        if copy_from is None:
            self.cols = cols
            self.rows = rows
            self.grid = self.generate_grid(initialize_with, values_max)
        else:
            self.grid = [[val for val in row] for row in copy_from]
            self.rows = len(copy_from)
            self.cols = len(copy_from[0])

    def generate_grid(self, value=None, values_max=9):
        if value is not None:
            # Fixed Value
            return [[value for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            # Random Values
            return [[randint(1, values_max) for _ in range(self.cols)] for _ in range(self.rows)]


    def __repr__(self):
        string = 'Grid: %dx%d\n' % (self.cols, self.rows)
        for row in self.grid:
            string += str(row) + '\n'
        return string

    def __getitem__(self, pt):
        if 0 <= pt.x < self.cols and 0 <= pt.y < self.rows:
            return self.grid[pt.y][pt.x]
        else:
            return 0
            # NOTE: Exceptions interfere with the iterative solution
            # raise IndexError

    def __setitem__(self, pt, value):
        if 0 <= pt.x < self.cols and 0 <= pt.y < self.rows:
            self.grid[pt.y][pt.x] = value
        else:
            raise IndexError

    def find_best_path(self, start, end):
        cache = Grid(self.cols, self.rows, initialize_with=-1)
        current = Point(end.x, end.y)
        # val = self.grid_path(current, start, cache)  # DP
        val = self.grid_path_iterative(current, start, cache)
        path = self.extract_best_path(current, start, cache)

        return val, path

    def extract_best_path(self, current, start, cache):
        stack = list()
        stack.append(current)

        while (current != start):
            print 'Stack:', stack
            print 'Current:', current

            left = Point(current.x-1, current.y)
            up = Point(current.x, current.y-1)

            if cache[left] > cache[up]:
                stack.append(left)
                current = left
            else:
                stack.append(up)
                current = up

        return stack[::-1]

    def grid_path(self, current, start, cache):
        # NOTE: state has cache.
        # Cache - Could alternatively be a part of the instance
        # But ensure there are no cyclic dependencies; Chache having a cache, ...
        # Ideally, matrix should be a separate Class
        # Grid could contain a Matrix grid as well as a Matrix Cache

        # Guard stays outside the
        if current.x < 0 or current.y < 0:
            return 0

        # if cache is empty
        if cache[current] == -1:
            print 'Current: (%d,%d) [%d]' % (current.x, current.y, self[current])

            # Base
            if current.x == start.x and current.y == start.y:
                cache[current] = self[current]
            else:
                # Transition
                left = Point(current.x-1, current.y)
                up = Point(current.x, current.y-1)

                # Update Cache + Min/Max Transition
                cache[current] = self[current] + max(
                    self.grid_path(left, start, cache),
                    self.grid_path(up, start, cache)
                )

        return cache[current]

    def grid_path_iterative(self, end, start, cache):
        # Storage is Row Major order; Thus row computation is inside
        # Cache Hit optimization
        for x in range(self.cols):
            for y in range(self.rows):
                current = Point(x,y)

                if current.x < 0 or current.y < 0:
                    return 0

                print 'Current: (%d,%d) [%d]' % (current.x, current.y, self[current])

                # Base
                if current.x == start.x and current.y == start.y:
                    cache[current] = self[current]
                else:
                    # Transition
                    left = Point(current.x-1, current.y)
                    up = Point(current.x, current.y-1)

                    # Update Cache + Min/Max Transition
                    cache[current] = self[current] + max(
                        cache[left],
                        cache[up]
                    )

        return cache[end]


    def grid_path_recursion(self, current, start):
        print 'Current: (%d,%d) [%d]' % (current.x, current.y, self[current])

        if current.x < 0 or current.y < 0:
            return 0

        if current.x == start.x and current.y == start.y:
            return self[current]

        return self[current] + max(
            self.grid_path(Point(current.x-1, current.y), start),
            self.grid_path(Point(current.x, current.y-1), start)
        )


def main():
    grid = Grid(copy_from=initialized)
    start = Point(0,0)
    end = Point(grid.cols-1, grid.rows-1)
    cost, path = grid.find_best_path(start, end)

    print 'Grid:', grid
    print 'Cost:', cost
    print 'Path:', path

if __name__ == '__main__':
    main()
