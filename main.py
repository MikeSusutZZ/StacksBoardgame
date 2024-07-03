from piece import Piece
from board import Board

def main():
    piece1 = Piece(1, "Player1")
    piece2 = Piece(2, "Player2")
    
    board = Board()
    board.place_piece(piece1, 2, 3)
    board.place_piece(piece2, 0, 0)
    
    print(board)

if __name__ == "__main__":
    main()
