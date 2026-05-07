from dataclasses import dataclass, field
from skyjo.game.constants import CARD_DISTRIBUTION
from skyjo.game.card import Card
from random import shuffle


@dataclass()
class Deck:
    """
    Represent the deck in the game of Skyjo.

    A deck contains 150 cards with values from -2 to 12,
    distributed according to SkyJo rules.

    Attributes:
        deck: List of Card objects in the deck
    """

    deck: list = field(default_factory=list)

    def __post_init__(self) -> None:
        for card_value in CARD_DISTRIBUTION.keys():
            for _ in range(CARD_DISTRIBUTION.get(card_value)):
                new_card = Card(card_value)
                self.deck.append(new_card)
        shuffle(self.deck)

    def shuffle(self) -> None:
        """Shuffle the deck"""
        shuffle(self.deck)

    def draw(self) -> Card:
        """
        Draw a card from the top of the deck.

        Returns:
            Card: The drawn card

        Raises:
            IndexError: If attempting to draw from an empty deck
        """
        if self.is_empty():
            raise IndexError("Cannot draw from empty deck")
        card = self.deck.pop()
        card.reveal()
        return card


    def is_empty(self) -> bool:
        """
        Check if the deck is empty
        Returns:
            True if the deck is empty

        """
        return len(self.deck) == 0

    def cards_remaining(self) -> int:
        return len(self.deck)
