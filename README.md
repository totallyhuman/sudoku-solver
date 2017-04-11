# sudoku-solver
A solver for Sudoku puzzles written in Python. Not guaranteed to find a
solution.

Depends on [`colorama`](https://github.com/tartley/colorama/).

## How does it solve puzzles?
It employs a "greedy" algorithm which means it calculates all possibilities for
a cell and continuously narrows them down. It solves easier puzzles fast
while it does not solve harder puzzles at all.

## Why?
Why not?
