#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict

class Sudoku(object):
    """
    Sudoku(values) -> new instance

    A class for a Sudoku puzzle.

    Keyword arguments:
    values   -- an array containing all 81 values of a puzzle horizontally

    Instance variables:
    values   -- an array containing all 81 values of a puzzle horizontally
    rows     -- a multi-dimensional array that stores 9 rows as arrays, each
                holding 9 values
    columns  -- a multi-dimensional array that stores 9 columns as arrays, each
                holding 9 values
    squares  -- a multi-dimensional array that stores 9 3x3 squares as arrays,
                each holding 9 values
    """
    values = []
    rows = [[], [], [], [], [], [], [], [], []]
    columns = [[], [], [], [], [], [], [], [], []]
    squares = [[], [], [], [], [], [], [], [], []]
    grid = OrderedDict()

    def __init__(self, values):
        """See class docstring for details."""
        self.values = values

    def parse_sudoku(self):
        """Calls the parse methods for converting the values into arrays."""
        self.parse_rows()
        self.parse_columns()
        self.parse_squares()
        self.parse_grid()

    def parse_rows(self):
        """Parses the values into the rows array."""
        for i in range(9):
            for j in self.values[i * 9:i * 9 + 9]:
                self.rows[i].append(j)

    def parse_columns(self):
        """Parses the rows into the columns array."""
        for row in self.rows:
            for i in range(9):
                self.columns[i].append(row[i])

    def parse_squares(self):
        """Parses the rows into the squares array."""
        for i in range(9):
            for j in range(0, 3):
                for k in range(0, 3):
                    self.squares[i].append(self.rows[j][k])

    def parse_grid(self):
        for l in 'ABCDEFGHI':
            for i in range(1, 10):
                self.grid[l + str(i)] = ''

# An example sudoku stored as an 81 value array
values = [0, 0, 0, 2, 6, 0, 7, 0, 1,
          6, 8, 0, 0, 7, 0, 0, 9, 0,
          1, 9, 0, 0, 0, 4, 5, 0, 0,
          8, 2, 0, 1, 0, 0, 0, 4, 0,
          0, 0, 4, 6, 0, 2, 9, 0, 0,
          0, 5, 0, 0, 0, 3, 0, 2, 8,
          0, 0, 9, 3, 0, 0, 0, 7, 4,
          0, 4, 0, 0, 5, 0, 0, 3, 6,
          7, 0, 3, 0, 1, 8, 0, 0, 0]

# Answer to example sudoku:
# 4  3  5 | 2  6  9 | 7  8  1
# 6  8  2 | 5  7  1 | 4  9  3
# 1  9  7 | 8  3  4 | 5  6  2
# --------+---------+--------
# 8  2  6 | 1  9  5 | 3  4  7
# 3  7  4 | 6  8  2 | 9  1  5
# 9  5  1 | 7  4  3 | 6  2  8
# --------+---------+--------
# 5  1  9 | 3  2  6 | 8  7  4
# 2  4  8 | 9  5  7 | 1  3  6
# 7  6  3 | 4  1  8 | 2  5  9

# Creates a new instance of the Sudoku class passing the values array
sudoku = Sudoku(values)
sudoku.parse_grid()
print(sudoku.grid)
