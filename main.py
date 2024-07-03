from piece import Piece
from board import Board
from stack import Stack

def main():
    piece1 = Piece(1, "Player1")
    piece2 = Piece(2, "Player2")
    
    board = Board()
    board.place_piece(piece1, 2, 3)
    board.place_piece(piece2, 0, 0)
    
    print("Initial board:")
    print(board)

    while True:
        try:
            from_coords = input("Enter the coordinates of the piece to move (format: x,y): ")
            to_coords = input("Enter the destination coordinates (format: x,y): ")

            from_x, from_y = map(int, from_coords.split(','))
            to_x, to_y = map(int, to_coords.split(','))

            board.move(from_x, from_y, to_x, to_y)
            print("Board after move:")
            print(board)

            add_stack = input("Do you want to add a stack to a piece? (y/n): ").strip().lower()
            if add_stack == 'y':
                piece_coords = input("Enter the coordinates of the piece to add a stack (format: x,y): ")
                x, y = map(int, piece_coords.split(','))
                stack_type = input("Enter the stack type (atk, def, spd, atk-, def-, spd-, null): ").strip()
                piece = board.grid[x][y]
                if piece:
                    piece.add_stack(Stack(stack_type))
                    print(f"Updated piece: {piece}")
                else:
                    print("No piece at the specified coordinates")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        cont = input("Do you want to make another move? (y/n): ").strip().lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()
