#!/usr/bin/env python2

def get_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                # print 'get_empty: [%d,%d]' % (i, j)
                yield (i, j)
    # return (None, None)

def print_sudoku(grid, title=None):
    if title is not None:
        print title
    for i in range(9):
        print ' '.join(str(j) for j in grid[i])


def isValid(grid, r, c, value):
    # Check Row
    for i in range(9):
        if grid[i][c] == value:
            # print 'Row Check Failed! Grid[%d,%d] = %d' % (r,c,value)
            return False

    # Check Col
    for i in range(9):
        if grid[r][i] == value:
            # print 'Col Check Failed! Grid[%d,%d] = %d' % (r,c,value)
            return False

    # Check Cube
    rstart = r - r%3
    cstart = c - c%3

    for i in range(rstart, rstart+3):
        for j in range(cstart, cstart+3):
            if grid[i][j] == value:
                # print 'Cube Check Failed! Grid[%d,%d] = %d' % (r,c,value)
                return False

    # print_sudoku(grid, 'isValid')
    # print ('Grid[%d,%d] = %d' % (r,c,value))
    return True


def sudoku_solve(grid):
    """
        Validates whether the grid is solvable and prints a valid output.
        Given the constraints of the input, this should never return a False.
    """
    # print_sudoku(grid, 'Sudoku Solve')
    try:
        (r,c) = get_empty(grid).next()  # NOTE: when getting one item
    except StopIteration:
        # Base
        print_sudoku(grid)
        return True

    # Transitions
    for value in range(1, 9+1):
        # print 'Considering value:', value
        if isValid(grid, r, c, value):
            grid[r][c] = value
            if sudoku_solve(grid):
                return True

    grid[r][c] = 0

    return False

def main():
    # Boiler Plate
    n = input()

    for i in range(n):
        board = []
        for j in range(9):
            board.append([int(k) for k in raw_input().split()])

        sudoku_solve(board)


if __name__ == '__main__':
    main()
