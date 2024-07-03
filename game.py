class Game (object):
    def __init__(self):
        self.grid = [[None for _ in range(5)] for _ in range(5)]
    def place_piece(self, piece, x, y):
        if 0 <= x < 5 and 0 <= y < 5 and self.grid[x][y] is None:
            self.grid[x][y] = piece
        else:
            raise ValueError("Invalid position or position already occupied")
        
    def move(self, from_x, from_y, to_x, to_y):
        if not (0 <= from_x < 5 and 0 <= from_y < 5):
            raise ValueError("Invalid 'from' position")
        if not (0 <= to_x < 5 and 0 <= to_y < 5):
            raise ValueError("Invalid 'to' position")
        if self.grid[from_x][from_y] is None:
            raise ValueError("No piece at 'from' position")
        if self.grid[to_x][to_y] is not None:
            raise ValueError("Destination position already occupied")
        self.grid[to_x][to_y] = self.grid[from_x][from_y]
        self.grid[from_x][from_y] = None

    def start(self):


    def __repr__(self):
        board_repr = ""
        for row in self.grid:
            for piece in row:
                if piece is None:
                    board_repr += " - "
                else:
                    board_repr += " " + piece.symbol + " "
            board_repr += "\n"
        return board_repr