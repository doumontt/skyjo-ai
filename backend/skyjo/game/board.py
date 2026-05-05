from skyjo.game.card import Card
from skyjo.game.deck import Deck
from skyjo.game.constants import NBR_COL, NBR_LINES
from dataclasses import dataclass
from typing import List, Optional


class Board:
    """
    Represent the board of a specific player in the game of SkyJo
    The board is a nbr_lines * nbr_columns arrangement of cards
    Attributes:

    """

    def __init__(self, card: List[Card]):
        pass
