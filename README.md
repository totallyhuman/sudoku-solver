# sudoku-solver
A solver for Sudoku puzzles written in Python. Not guaranteed to find a
solution.

Depends on [`colorama`](https://github.com/tartley/colorama/).

## How does it solve puzzles?
It employs a "greedy" algorithm which means it calculates all possibilities for
a cell and continuously narrows them down. It solves easier puzzles fast
while it does not solve harder puzzles at all.

## How do you use it?
It currently takes no input; the Sudoku puzzle being solved is hard coded. This will probably be changed in the near future.

## Why?
Why not?
