class Stack:
    """
    A class to represent a stat change stack.
    
    Attributes:
    -----------
    type : str
        The type of the stack ('atk', 'def', 'spd', 'atk-', 'def-', 'spd-', 'null').
    """
    def __init__(self, stack_type):
        """
        Initializes a new stat change stack.
        
        Parameters:
        -----------
        stack_type : str
            The type of the stack.
        """
        self.type = stack_type

    def apply(self, atk, def_, spd):
        """
        Applies the stat change to the given stats.
        
        Parameters:
        -----------
        atk : int
            The attack stat.
        def_ : int
            The defense stat.
        spd : int
            The speed stat.
        
        Returns:
        --------
        (int, int, int)
            The modified attack, defense, and speed stats.
        """
        if self.type == 'atk':
            atk += 1
        elif self.type == 'def':
            def_ += 1
        elif self.type == 'spd':
            spd += 1
        elif self.type == 'atk-':
            atk -= 1
        elif self.type == 'def-':
            def_ -= 1
        elif self.type == 'spd-':
            spd -= 1
        return atk, def_, spd

    def __repr__(self):
        return f"Stack(type={self.type})"
