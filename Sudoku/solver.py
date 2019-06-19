"""
Contains a function which will take a puzzle and return a solved version.

The blanks in the input puzzles should be zeroes.
"""

from .sudoku import SudokuPuzzle

def all_solutions_iter(blank: SudokuPuzzle):
    """
    Takes a puzzle with blanks as zeroes and yields all possible solutions
    """

    # List the coordinates of all blanks
    blank_coords = []
    for i in range(len(blank.table)):
        for j in range(len(blank.table[0])):
            if blank.table[i][j] == 0:
                blank_coords.append((i, j))

    # If no blanks are left, just return this one if it is valid
    if len(blank_coords) == 0:
        if blank.is_valid():
            return [blank]
        else:
            return []


    # Take the first away, and for each possible value it could hold, solve
    # the problem for the rest of the list
    first_coord, *other_coords = blank_coords
    for value in range(1, blank.width + 1):
        # Do this once for each possible value

        # Fill the value in
        blank.table[first_coord[0]][first_coord[1]] = value

        # Solve the smaller problem
        yield from all_solutions_iter(blank)


def all_solutions(blank: SudokuPuzzle):
    """Returns a list of all possible solutions to the puzzle"""
    return list(all_solutions_iter(blank))