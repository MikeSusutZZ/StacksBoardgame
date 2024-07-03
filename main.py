from piece import Piece
from board import Board
from game import Game

def main():
    game = Game()
    game.start()
    # piece1 = Piece(1, "P1")
    # piece2 = Piece(2, "P2")

    
    # board = Board()
    # board.place_piece(piece1, 2, 3)
    # board.place_piece(piece2, 0, 0)
    
    # print("Initial board:")
    # print(board)

    # while True:
    #     try:
    #         from_coords = input("Enter the coordinates of the piece to move (format: x,y): ")
    #         to_coords = input("Enter the destination coordinates (format: x,y): ")

    #         from_x, from_y = map(int, from_coords.split(','))
    #         to_x, to_y = map(int, to_coords.split(','))

    #         board.move(from_x, from_y, to_x, to_y)
    #         print("Board after move:")
    #         print(board)
    #     except ValueError as e:
    #         print(f"Error: {e}")
    #     except Exception as e:
    #         print(f"Unexpected error: {e}")

    #     cont = input("Do you want to make another move? (y/n): ").strip().lower()
    #     if cont != 'y':
    #         break

if __name__ == "__main__":
    main()
