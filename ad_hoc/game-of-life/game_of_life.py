#!/usr/bin/env python2

def count_neighbours(grid, r, c):
    delta = [(1, 1), (1, -1), (-1, 1), (-1, -1),
             (1, 0), (0, 1), (-1, 0), (0, -1)]

    R = len(grid)
    C = len(grid[0])

    count = 0
    for d in delta:
        nr = r + d[0]
        nc = c + d[1]

        if 0 <= nr < R and 0 <= nc < C:
            count += grid[nr][nc]

    return count


def simulate_step(grid):
    board = [[0] * len(grid[0]) for _ in range(len(grid))]
    isAlive = True

    print_board(grid, 'Init:')

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            count = count_neighbours(grid, r, c)
            print '[%d, %d]: count(%d)' % (r, c, count),

            if cell == 0:
                if count == 3:
                    board[r][c] = 1
                    print '0 -> 1'
                else:
                    print '0 -> 0'
                    isAlive = False
            else:  # Cell is Alive
                if count < 2 or count > 3:
                    board[r][c] = 0
                    isAlive = False
                    print '1 -> 0'
                else:
                    board[r][c] = cell
                    print '%d -> %d' % (cell, cell)
    return board, isAlive


def print_board(board, string=''):
    print '\n' + string
    for row in board:
        print row

def main(grid):
    board, isAlive = simulate_step(grid)
    print_board(board, 'Result:')

    return isAlive

if __name__ == '__main__':
    cases = input()

    for case in range(1, cases+1):
        grid = list()
        row, col = [int(x) for x in raw_input().split()]

        for _ in range(row):
            grid.append([int(x) for x in raw_input().split()])

        isAlive = main(grid)
        result = 'alive' if isAlive else 'dead'
        print 'Case #%d: %s' % (case, result)
