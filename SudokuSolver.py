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
    rows     -- a two-dimensional array that stores 9 rows as arrays, each
                holding 9 values
    columns  -- a two-dimensional array that stores 9 columns as arrays, each
                holding 9 values
    squares  -- a two-dimensional array that stores 9 3x3 squares as arrays,
                each holding 9 values
    """
    values = []
    rows = [[], [], [], [], [], [], [], [], []]
    columns = [[], [], [], [], [], [], [], [], []]
    squares = []
    grid = OrderedDict()

    def __init__(self, values):
        """See class docstring for details."""
        self.values = values

    def parse_sudoku(self, v, grid = True):
        """Calls the parse methods for converting the values into arrays."""
        v = list(v)

        self.values = v
        self.rows = [[], [], [], [], [], [], [], [], []]
        self.columns = [[], [], [], [], [], [], [], [], []]
        self.squares = []

        self.parse_rows(v)
        self.parse_columns()
        self.parse_squares()
        if grid: self.parse_grid(v)

    def parse_rows(self, v):
        """Parses the values into the rows array."""
        for i in range(9):
            for j in v[i * 9:i * 9 + 9]:
                if type(j) is int: self.rows[i].append(j)
                else: self.rows[i].append(0)

    def parse_columns(self):
        """Parses the rows into the columns array."""
        for row in self.rows:
            for i in range(9):
                self.columns[i].append(row[i])

    def parse_squares(self):
        """Parses the rows into the squares array."""
        for square_x in range(0, 7)[::3]:
            for square_y in range(0, 7)[::3]:
                square = []
                for x in range(3):
                    for y in range(3):
                        square.append(self.rows[square_x + x][square_y + y])
                self.squares.append(square)

    def parse_grid(self, v):
        """Parses the values into the grid dict."""
        j = 0
        for l in 'ABCDEFGHI':
            for i in range(1, 10):
                self.grid[l + str(i)] = v[j]
                j += 1

    def locate_cell(self, cell):
        """Given a cell index, returns the units the cell is in."""
        location = []
        x = int(cell[1]) - 1
        y = ord(cell[0]) - 65

        location.append(self.rows[y])
        location.append(self.columns[x])

        if y in range(3):
            if x in range(3): location.append(self.squares[0])
            elif x in range(3, 6): location.append(self.squares[1])
            elif x in range(6, 9): location.append(self.squares[2])
        elif y in range(3, 6):
            if x in range(3): location.append(self.squares[3])
            elif x in range(3, 6): location.append(self.squares[4])
            elif x in range(6, 9): location.append(self.squares[5])
        elif y in range(6, 9):
            if x in range(3): location.append(self.squares[6])
            elif x in range(3, 6): location.append(self.squares[7])
            elif x in range(6, 9): location.append(self.squares[8])

        return location

    def calculate_possibilities(self):
        """For each empty cell, find numbers that are not in its units."""
        did_something = False
        print("Calculating possibilities...")

        for key, value in self.grid.items():
            if value == 0 or type(value) is list:
                self.grid[key] = []
                location = self.locate_cell(key)

                for i in range(1, 10):
                    if (i not in location[0] and i not in location[1] and i
                                                           not in location[2]):
                        self.grid[key].append(i)
                        did_something = True
                if len(self.grid[key]) == 1: self.grid[key] = self.grid[key][0]

        return did_something

    def solve(self):
        """Calculates all possibilities and continuously narrows them down."""
        while True:
            did_something = self.calculate_possibilities()
            self.parse_sudoku(self.grid.values(), grid = False)
            if not did_something: break

    @staticmethod
    def format(v):
        """Format a sudoku puzzle and print it out."""
        for i, j in enumerate(v):
            if j == 0:
                v[i] = ' '
        print(' %s  %s  %s | %s  %s  %s | %s  %s  %s\n'
              ' %s  %s  %s | %s  %s  %s | %s  %s  %s\n'
              ' %s  %s  %s | %s  %s  %s | %s  %s  %s\n'
              ' --------+---------+--------\n'
              ' %s  %s  %s | %s  %s  %s | %s  %s  %s\n'
              ' %s  %s  %s | %s  %s  %s | %s  %s  %s\n'
              ' %s  %s  %s | %s  %s  %s | %s  %s  %s\n'
              ' --------+---------+--------\n'
              ' %s  %s  %s | %s  %s  %s | %s  %s  %s\n'
              ' %s  %s  %s | %s  %s  %s | %s  %s  %s\n'
              ' %s  %s  %s | %s  %s  %s | %s  %s  %s\n' % tuple(v))

values = [0, 0, 0, 2, 6, 0, 7, 0, 1,
          6, 8, 0, 0, 7, 0, 0, 9, 0,
          1, 9, 0, 0, 0, 4, 5, 0, 0,
          8, 2, 0, 1, 0, 0, 0, 4, 0,
          0, 0, 4, 6, 0, 2, 9, 0, 0,
          0, 5, 0, 0, 0, 3, 0, 2, 8,
          0, 0, 9, 3, 0, 0, 0, 7, 4,
          0, 4, 0, 0, 5, 0, 0, 3, 6,
          7, 0, 3, 0, 1, 8, 0, 0, 0]

def main():
    print('Sudoku Solver\n=============\n')
    sudoku = Sudoku(values)
    sudoku.parse_sudoku(values)
    sudoku.solve()
    print('\n')
    sudoku.format(values)
    print(" ->\n")
    sudoku.format(sudoku.values)

if __name__ == '__main__':
    main()
