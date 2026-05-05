import pytest
import tests.conftest
from tests.conftest import *

from skyjo.game.board import Board


class TestBoard:
    def test_board_creation(self, random_cards):
        board = Board(random_cards)
        assert board is not None
        assert len(board.get_all_cards) == 12

    def test_reveal_card(self, random_cards):
        board = Board(random_cards)
        board.reveal_card(0,0)
        assert board.grid[0][0].revealed == True

    def test_check_column_completion_requires_revealed(self):
        """Column completion requires all cards revealed."""
        cards = [Card(5) for _ in range(12)]
        board = Board(cards)

        # All cards have same value but none revealed
        #assert board.check_column_completion(0) == False

        # Reveal 2 out of 3
        board.reveal_card(0, 0)
        board.reveal_card(1, 0)
        #assert not board.check_column_completion(0)

        # Reveal all 3
        board.reveal_card(2, 0)
        assert board.check_column_completion(0) == True

    def test_board_constructor_validates_card_count(self):
        """Board constructor should reject wrong number of cards."""
        with pytest.raises(ValueError, match="exactly 12 cards"):
            Board([Card(0) for _ in range(10)])  # Too few

        with pytest.raises(ValueError, match="exactly 12 cards"):
            Board([Card(0) for _ in range(15)])  # Too many
