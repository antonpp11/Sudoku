#!/usr/local/bin/python3

import numpy as np
import time


class Solver():
    def __init__(self, grid):
        self.grid = grid


def possible(y, x, n):
    for i in range(9):
        if table[y][i] == n:
            return False
    for i in range(9):
        if table[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if table[y0 + i][x0 + j] == n:
                return False
    return True


def solve(table):
    for y in range(9):
        for x in range(9):
            if table[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        table[y][x] = n
                        solve(table)
                        table[y][x] = 0
                return
    print(np.matrix(table))


if __name__ == '__main__':
    global table
    table = [[6, 0, 0, 0, 7, 1, 4, 0, 0],
             [0, 0, 0, 9, 0, 4, 0, 0, 3],
             [0, 4, 3, 0, 0, 0, 7, 0, 0],
             [2, 0, 0, 5, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 7, 6, 5, 0],
             [0, 0, 9, 0, 3, 0, 0, 0, 0],
             [7, 3, 2, 0, 1, 0, 8, 0, 0],
             [0, 0, 0, 0, 0, 0, 2, 0, 4],
             [0, 0, 0, 0, 2, 6, 9, 0, 0]]
    timestamp1 = time.time()
    print(np.matrix(table))
    print()
    solve(table)
    timestamp2 = time.time()
    print(f"This took {timestamp2 - timestamp1} seconds")
    # time.sleep()
