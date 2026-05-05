from skyjo.game.card import Card
from skyjo.game.constants import NBR_COL, NBR_ROWS


class Board:
    """
    Represent the board of a specific player in the game of SkyJo
    The board is a nbr_lines * nbr_columns arrangement of cards
    Attributes:

    """
    grid: list[list[Card|None]]
    def __init__(self, cards: list[Card]):
        expected_count = NBR_ROWS * NBR_COL
        if len(cards) != expected_count:
            raise ValueError(
                f"Board requires exactly {expected_count} cards, got {len(cards)}"
            )
        self.grid = [cards[i:i + NBR_COL] for i in range(0, len(cards), NBR_COL)]

    def reveal_card(self, row: int, col: int) -> Card:
        """
        Reveal the card at coordinates row, col

        Parameters:
            row, col:
                The row and column of the card that is revealed, 0-indexed

        Returns:
            Card: The revealed card

        Raises:
            IndexError: If attempting to reveal a card which is not on the board
            OtherError: If attempting to reveal a card which is already revealed

        """
        if not 0 <= row < NBR_ROWS or not 0 <= col < NBR_COL:
           raise IndexError("Cannot reveal a card outside the board")

        card = self.grid[row][col]
        if card is None:
            raise IndexError("Cannot reveal a card in a column that has been eliminated")
        if card.revealed:
            raise ValueError(f"Card at position ({row}, {col}) is already revealed")
        else:
            card.reveal()
        return card


    def replace_card(self, row: int, col: int, new_card: Card) -> Card:
        """
        Replace the card at row, col by a new card
        Args:
            row: Row of the card to be replaced
            col: Column of the card to be replaced
            new_card: New card to put in the position

        Returns: The card that was replaced

        Raises: Index Error: If attempting to remove a card that does not exist
                Value Error: If attempting to replace a card that has been removed

        """
        if not 0 <= row < NBR_ROWS or not 0 <= col < NBR_COL:
           raise IndexError("Cannot change with a card outside the board")
        if self.grid[row][col] is None:
            raise ValueError("Cannot change with a card that has been eliminated")
        old_card, self.grid[row][col] = self.grid[row][col], new_card
        assert old_card is not None
        return old_card

    def check_column_completion(self, col: int) -> bool:
        """
        Check if a column is constituted of cards of the same values that are revealed
        Args:
            col: The column to check

        Returns:
            True if the column is complete

        Raises:
            IndexError: If trying to access a column outside the board

        """
        if not 0 <= col < NBR_COL:
            raise IndexError(f"Column {col} is outside the board")

        column_cards = [self.grid[row][col] for row in range(NBR_ROWS)]

        if any(card is None for card in column_cards):
            return False

        #Avoid type mistakes by ensuring the column_cards doesn't contain any None
        column_cards = [card for card in column_cards if card is not None]

        if not all(card.revealed for card in column_cards):
            return False

        return len({card.value for card in column_cards}) == 1

    def remove_column(self, col: int) -> list[Card]:
        """
        Remove the Cards of a specific column from the board
        Args:
            col: The column to remove

        Returns:
            A list of cards that have been removed

        """
        stack = []
        for row in range(NBR_ROWS):
            stack.append(self.grid[row][col])
            self.grid[row][col] = None
        return stack

    def get_card(self, row, col) -> Card|None:
        """
        Return the card at row, col, or None if the card has been removed

        Returns:
            The Card at row, col or None

        """
        if not 0 <= row < NBR_ROWS or not 0 <= col < NBR_COL:
           raise IndexError(f"Cannot access the card at {row},{col}: It is outside the board")
        return self.grid[row][col]

    @property
    def get_all_cards(self) -> list[Card|None]:
        stack = []
        for row in self.grid:
            stack.extend(row)
        return stack

    def all_revealed(self) -> bool:
        """Return true if all cards on this board are None or revealed"""
        for card in self.get_all_cards:
            if card is not None and not card.revealed:
                return False
        return True

    def __str__(self) -> str:
        """String representation of the board."""
        lines = []
        for row in self.grid:
            row_str = " ".join(str(card) if card else "[XXX]" for card in row)
            lines.append(row_str)
        return "\n".join(lines)

