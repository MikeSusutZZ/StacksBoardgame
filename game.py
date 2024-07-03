from board import Board
from piece import Piece
from constants import BOARD_SIZE

class Game (object):
    def __init__(self):
        self.board = Board()
        for i in range(BOARD_SIZE):
            self.board.place_piece(Piece(i, "P1"), 0, i)
            self.board.place_piece(Piece(i, "P2"), 4, i)

    def start(self):
        while True:
            print(self.board)
            from_coords = input("Enter the coordinates of the piece to move (format: x,y): ")
            to_coords = input("Enter the destination coordinates (format: x,y): ")

            from_x, from_y = map(int, from_coords.split(','))
            to_x, to_y = map(int, to_coords.split(','))

            try:
                self.board.move(from_x, from_y, to_x, to_y)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

            cont = input("Do you want to make another move? (y/n): ").strip().lower()
            if cont != 'y':
                break

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