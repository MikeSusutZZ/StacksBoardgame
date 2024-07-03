class Piece:
    """
    A class to represent a game piece.
    
    Attributes:
    -----------
    id : int
        The identifier for the piece.
    owner : str
        The owner of the piece.
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

    def __repr__(self):
        return f"Piece(id={self.id}, owner={self.owner})"
