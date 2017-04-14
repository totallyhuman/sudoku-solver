# Sudoku Solver

## Classes
### Sudoku(values)

A class for a Sudoku puzzle.

Arguments:
* values -- a list containing the 81 values of a puzzle horizontally

Instance variables:
* values -- a list containing the 81 values of a puzzle horizontally
* rows -- a two-dimensional list that stores 9 rows as lists, each holding 9 values
* columns -- a two-dimensional list that stores 9 columns as lists, each holding 9 values
* squares -- a two-dimensional list that stores 9 3x3 squares as lists, each holding 9 values

Returns an instance of the Sudoku class.

## Functions
### Sudoku.\_\_init\_\_
`__init__(values)`:

See class docstring for details.

### Sudoku.parse\_sudoku
`parse_sudoku(v, grid)`:

Calls the parse methods for converting the values into lists.

Arguments:
* v -- a list containing the 81 values of a puzzle horizontally
* grid -- a boolean which determines if parse_grid() is run (defaults to True)

### Sudoku.parse\_rows
`parse_rows(v)`:

Parses the values into the rows list.

Arguments:
* v -- a list containing the 81 values of a puzzle horizontally

### Sudoku.parse\_columns
`parse_columns()`:

Parses the rows into the columns list.

### Sudoku.parse\_squares
`parse_squares()`:

Parses the rows into the squares list.

### Sudoku.parse\_grid
`parse_grid(v)`:

Parses the values into the grid dict.

Arguments:
* v -- a list containing the 81 values of a puzzle horizontally

### Sudoku.locate\_cell
`locate_cell(cell)`:

Given a cell index, returns the units the cell is in.

Arguments:
* cell -- a string containing the index of a puzzle cell

Returns:
* location -- a list containing the units the given cell is in

### Sudoku.calculate\_possibilities
`calculate_possibilities()`:

For each empty cell, find numbers that are not in its units.

Returns:
* did_something -- a boolean which stores if the function made any changes to a cell

### Sudoku.solve
`solve()`:

Calculates all possibilities and continuously narrows them down.

### Sudoku.format
`format(v)`:

Format a sudoku puzzle.

Arguments:
* v -- a list containing the 81 values of a puzzle horizontally

Returns:
* result -- a string that is a visually formatted version of the values.

### main
`main()`:

Main function that creates a Sudoku object and prints the solution out.
