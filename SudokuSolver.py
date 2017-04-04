#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_rows(values):
    for i in range(0, 8):
        for j in values[i * 9:i * 9 + 9]:
            rows[i].append(j)

def get_columns(rows):
    for row in rows:
        for i in range(0, 8):
            columns[i].append(row[i])

def get_squares(rows):
    for i in range(0, 8):
        for j in range(0, 3):
            for k in range(0, 3):
                squares[i].append(rows[j][k])

rows = [[], [], [], [], [], [], [], [], []]
columns = [[], [], [], [], [], [], [], [], []]
squares = [[], [], [], [], [], [], [], [], []]

values = [0, 0, 0, 2, 6, 0, 7, 0, 1,
          6, 8, 0, 0, 7, 0, 0, 9, 0,
          1, 9, 0, 0, 0, 4, 5, 0, 0,
          8, 2, 0, 1, 0, 0, 0, 4, 0,
          0, 0, 4, 6, 0, 2, 9, 0, 0,
          0, 5, 0, 0, 0, 3, 0, 2, 8,
          0, 0, 9, 3, 0, 0, 0, 7, 4,
          0, 4, 0, 0, 5, 0, 0, 3, 6,
          7, 0, 3, 0, 1, 8, 0, 0, 0]
