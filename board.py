from piece import Piece
from constants import BOARD_SIZE

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
        self.grid = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

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

    def move(self, from_x, from_y, to_x, to_y):
        """
        Moves a piece from one coordinate to another.
        
        Parameters:
        -----------
        from_x : int
            The x-coordinate (row) of the piece to move.
        from_y : int
            The y-coordinate (column) of the piece to move.
        to_x : int
            The x-coordinate (row) where the piece will be moved.
        to_y : int
            The y-coordinate (column) where the piece will be moved.
        """
        if not (0 <= from_x < 5 and 0 <= from_y < 5):
            raise ValueError("Invalid 'from' position")
        if not (0 <= to_x < 5 and 0 <= to_y < 5):
            raise ValueError("Invalid 'to' position")
        if self.grid[from_x][from_y] is None:
            raise ValueError("No piece at 'from' position")
        if self.grid[to_x][to_y] is not None:
            if self.grid[to_x][to_y].owner == self.grid[from_x][from_y].owner:
                raise ValueError("Cannot move to a position occupied by your own piece")

            # Check for capture
            attacker = self.grid[from_x][from_y]
            defender = self.grid[to_x][to_y]
            if attacker.atk >= defender.def_:
                # Capture the piece
                self.grid[to_x][to_y] = attacker
                self.grid[from_x][from_y] = None
                print(f"Piece {defender} captured by {attacker}")
            else:
                # Do not move and pop a stack from the defender
                if defender.stacks:
                    defender.stacks.pop()
                    defender.update_stats()
                    print(f"Defender {defender} lost a stack due to attack from {attacker}")
                else:
                    print(f"Defender {defender} has no stacks left to pop")
                return
        else:
            self.grid[to_x][to_y] = self.grid[from_x][from_y]
            self.grid[from_x][from_y] = None

    def __repr__(self):
        board_repr = ""
        for row in self.grid:
            board_repr += "[" + "\t|\t".join([f"O" if piece else "" for piece in row]) + "]" +  "\n"
        return board_repr
