from dataclasses import dataclass


@dataclass()
class Card:
    """
    Represent a single Card in the game of SkyJo
    Attributes:
        value: The value of the card, ranging from -2 to 12
        revealed: Whether the card is face-up
    """

    value: int
    revealed: bool = False

    def __post_init__(self):
        """Validate the card value"""
        if not -2 <= self.value <= 12:
            raise ValueError("f")

    def reveal(self) -> int:
        """Reveal this card"""
        self.revealed = True
        return self.value


    def __str__(self) -> str:
        """String representation of a card"""
        if self.revealed:
            return f"[{self.value:2d}]"
        else:
            return f"[ ?]"

    def __repr__(self) -> str:
        """Developer representation of a card"""
        return f"Card(Value={self.value}, revealed = {self.revealed})"
