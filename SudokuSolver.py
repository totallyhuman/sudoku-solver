#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import better_exceptions

class Sudoku(object):
    rows = [[], [], [], [], [], [], [], [], []]
    columns = [[], [], [], [], [], [], [], [], []]
    squares = [[], [], [], [], [], [], [], [], []]

    def __init__(self, values):
        self.get_rows(values)
        self.get_columns(self.rows)
        self.get_squares(self.rows)

    def get_rows(self, values):
        for i in range(0, 8):
            for j in values[i * 9:i * 9 + 9]:
                self.rows[i].append(j)

    def get_columns(self, rows):
        for row in self.rows:
            for i in range(0, 8):
                self.columns[i].append(row[i])

    def get_squares(self, rows):
        for i in range(0, 8):
            for j in range(0, 3):
                for k in range(0, 3):
                    self.squares[i].append(self.rows[j][k])

values = [0, 0, 0, 2, 6, 0, 7, 0, 1,
          6, 8, 0, 0, 7, 0, 0, 9, 0,
          1, 9, 0, 0, 0, 4, 5, 0, 0,
          8, 2, 0, 1, 0, 0, 0, 4, 0,
          0, 0, 4, 6, 0, 2, 9, 0, 0,
          0, 5, 0, 0, 0, 3, 0, 2, 8,
          0, 0, 9, 3, 0, 0, 0, 7, 4,
          0, 4, 0, 0, 5, 0, 0, 3, 6,
          7, 0, 3, 0, 1, 8, 0, 0, 0]

"""
Answer to example sudoku:
[4, 3, 5, 2, 6, 9, 7, 8, 1,
 6, 8, 2, 5, 7, 1, 4, 9, 3,
 1, 9, 7, 8, 3, 4, 5, 6, 2,
 8, 2, 6, 1, 9, 5, 3, 4, 7,
 3, 7, 4, 6, 8, 2, 9, 1, 5,
 9, 5, 1, 7, 4, 3, 6, 2, 8,
 5, 1, 9, 3, 2, 6, 8, 7, 4,
 2, 4, 8, 9, 5, 7, 1, 3, 6,
 7, 6, 3, 4, 1, 8, 2, 5, 9]
"""

sudoku = Sudoku(values)
