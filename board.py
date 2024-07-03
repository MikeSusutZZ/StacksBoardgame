from piece import Piece

class Board:
    """
    A class to represent a 5x5 game board.
    
    Attributes:
    -----------
    grid : list
        A 5x5 grid representing the board.
    """
    def __init__(self):
        """
        Initializes a new 5x5 game board.
        """
        self.grid = [[None for _ in range(5)] for _ in range(5)]

    def place_piece(self, piece, x, y):
        """
        Places a piece on the board at the specified coordinates.
        
        Parameters:
        -----------
        piece : Piece
            The piece to place on the board.
        x : int
            The x-coordinate (row) where the piece will be placed.
        y : int
            The y-coordinate (column) where the piece will be placed.
        """
        if 0 <= x < 5 and 0 <= y < 5 and self.grid[x][y] is None:
            self.grid[x][y] = piece
        else:
            raise ValueError("Invalid position or position already occupied")

    def __repr__(self):
        board_repr = ""
        for row in self.grid:
            board_repr += " | ".join([str(piece) if piece else " " for piece in row]) + "\n"
        return board_repr
