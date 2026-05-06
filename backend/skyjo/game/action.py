from dataclasses import dataclass
from enum import Enum

from pytokens.cli import validate

from skyjo.game.constants import NBR_COL, NBR_ROWS

class ActionType(Enum):
    REVEAL_CARD = "reveal_card" #To reveal cards on the board in the first round
    DRAW_FROM_DISCARD = "draw_from_discard"
    DRAW_FROM_DECK = "draw_from_deck"
    FLIP_CARD = "flip_card" #Discard drawn and reveal a card
    SWAP_CARD = "swap_card"


@dataclass
class Action:
    action: ActionType
    row: int = None
    col: int = None

    def __post_init__(self):
        self.validate()

    def validate(self) -> None:
        match self.action:
            case ActionType.REVEAL_CARD:
                if self.row is None or self.col is None:
                    raise ValueError(f"We need a position to reveal a card")
                if not 0<= self.row < NBR_ROWS or not 0<= self.col< NBR_COL:
                    raise IndexError(f"The Card at {self.row, self.col} is not on the Board")

            case ActionType.DRAW_FROM_DISCARD:
                if self.row is not None or self.col is not None:
                    raise ValueError(
                        f"Drawing from discard should not give position of card but {self.row, self.col} was given")

            case ActionType.DRAW_FROM_DECK:
                if self.row is not None or self.col is not None:
                    raise ValueError(
                        f"Drawing the top card of deck should not give position of card but {self.row, self.col} was given")

            case ActionType.FLIP_CARD:
                if self.row is None or self.col is None:
                    raise ValueError(
                        f"Drawing the top card of deck should not give position of card but {self.row, self.col} was given")
                if not 0 <= self.row < NBR_ROWS or not 0 <= self.col< NBR_COL:
                    raise IndexError(f"The Card at {self.row, self.col} is not on the Board")

            case ActionType.SWAP_CARD:
                if self.row is None or self.col is None:
                    raise ValueError(
                        f"Drawing the top card of deck should not give position of card but {self.row, self.col} was given")
                if not 0<= self.row < NBR_ROWS or not 0 <= self.col < NBR_COL:
                    raise IndexError(f"The Card at {self.row, self.col} is not on the Board")
