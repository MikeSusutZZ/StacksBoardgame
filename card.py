from constants import DEFAULT_STAT

class Card:
    def __init__(self, attack=DEFAULT_STAT, defense=DEFAULT_STAT, speed=DEFAULT_STAT, ):
        self.attack = DEFAULT_STAT # damage dealt to opponent
        self.defense = DEFAULT_STAT # damage resisted from opponent
        self.speed = DEFAULT_STAT # determines who goes first

    def __str__(self):
        return f"Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}"