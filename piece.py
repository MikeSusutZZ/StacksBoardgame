from stack import Stack

class Piece:
    """
    A class to represent a game piece.
    
    Attributes:
    -----------
    id : int
        The identifier for the piece.
    owner : str
        The owner of the piece.
    atk : int
        The attack stat of the piece.
    def_ : int
        The defense stat of the piece.
    spd : int
        The speed stat of the piece.
    stacks : list
        A list of stat change stacks.
    """
    def __init__(self, piece_id, owner):
        """
        Initializes a new game piece.
        
        Parameters:
        -----------
        piece_id : int
            The identifier for the piece.
        owner : str
            The owner of the piece.
        """
        self.id = piece_id
        self.owner = owner
        self.atk = 0
        self.def_ = 0
        self.spd = 0
        self.stacks = []

    def add_stack(self, stack):
        """
        Adds a stack to the piece.
        
        Parameters:
        -----------
        stack : Stack
            The stack to add.
        """
        self.stacks.append(stack)
        self.update_stats()

    def update_stats(self):
        """
        Updates the piece's stats based on the stacks.
        """
        self.atk, self.def_, self.spd = 0, 0, 0  # reset to base stats
        for stack in self.stacks:
            self.atk, self.def_, self.spd = stack.apply(self.atk, self.def_, self.spd)

    def __repr__(self):
        return (f"Piece(id={self.id}, owner={self.owner}, stacks={self.stacks})")
