"""
Defines a class for storing sudoku puzzles.
"""

from sys import stdout, stdin

class SudokuPuzzle:
    def __init__(self, size=3):
        """
        Defines a new puzzle. The given size will be squared to give the width/height.
        """

        self.size = size
        self.width = size ** 2

        # Generates a table, filled with zeroes, of size^2 width
        self.table = [[0 for _ in range(size ** 2)] for __ in range(size ** 2)]
    
    def is_valid(self):
        """Returns whether or not the puzzle is valid"""
        # Check each row for collisions
        for row in self.table:
            for num in range(1, self.width + 1):
                if row.count(num) > 1:
                    return False

        # Generate all columns and check there are no collisions
        for col_num in range(len(self.table[0])):
            col = []
            for row in self.table:
                col.append(row[col_num])
            for num in range(1, self.width + 1):
                if row.count(num) > 1:
                    return False

        # Loop through each big square
        # Check each one contains no more than one of each number
        for i in range(self.size):
            for j in range(self.size):
                # Picked an individual big square
                big_square = []
                # Add all items to it
                for k in range(self.size):  # Row
                    for l in range(self.size):  # Column
                        # Select the right individual square and add it to the list
                        big_square.append(self.table[3*i + k][3*j + l])
                
                # Check to make sure there are no repeats
                for num in range(1, self.width + 1):
                    if row.count(num) > 1:
                        return False
        
        # If all three tests passed, then the puzzle is valid
        return True

    def write(self, file=stdout):
        """Writes out a CSV version of the puzzle to the file"""
        for row in self.table:
            print(",".join(row), file=file)
    
    @staticmethod
    def read(file=stdin):
        """Reads in from the file (stream object) and returns a corresponding SudokuPuzzle"""
        # Read from the file and split into lines
        text = file.read()
        lines = text.split("\n")
        table = []

        # For each line, create a row and add it to the table
        for line in lines:
            row = []
            squares = line.split(",")
            for square in squares:
                row.append(int(square))
            table.append(row)
        
        # Turn from a list of lists into a puzzle
        puzzle = SudokuPuzzle()
        puzzle.table = table
        return puzzle