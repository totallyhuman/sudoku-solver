# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_columns(self, rows):
    for row in rows:
        for i in range(1, 9):
            columns[i].append(row[i])

rows = []
columns = [[], [], [], [], [], [], [], [], [], []]
rows[1] = [0, 0, 0, 2, 6, 0, 7, 0, 1]
rows[2] = [6, 8, 0, 0, 7, 0, 0, 9, 0]
rows[3] = [1, 9, 0, 0, 0, 4, 5, 0, 0]
rows[4] = [8, 2, 0, 1, 0, 0, 0, 4, 0]
rows[5] = [0, 0, 4, 6, 0, 2, 9, 0, 0]
rows[6] = [0, 5, 0, 0, 0, 3, 0, 2, 8]
rows[7] = [0, 0, 9, 3, 0, 0, 0, 7, 4]
rows[8] = [0, 4, 0, 0, 5, 0, 0, 3, 6]
rows[9] = [7, 0, 3, 0, 1, 8, 0, 0, 0]
