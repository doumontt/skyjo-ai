import pytest
from skyjo.game.action import Action, ActionType


class TestAction:
    """Test suite for Action class."""

    def test_create_reveal_card_action(self):
        """REVEAL_CARD requires position."""
        action = Action(ActionType.REVEAL_CARD, row=1, col=2)
        assert action.action == ActionType.REVEAL_CARD
        assert action.row == 1
        assert action.col == 2

    def test_reveal_card_without_position_fails(self):
        """REVEAL_CARD without position should raise error."""
        with pytest.raises(ValueError):
            Action(ActionType.REVEAL_CARD)

    def test_reveal_card_with_partial_position_fails(self):
        """REVEAL_CARD with only row or col should fail."""
        with pytest.raises(ValueError):
            Action(ActionType.REVEAL_CARD, row=1)

        with pytest.raises(ValueError):
            Action(ActionType.REVEAL_CARD, col=2)

    def test_draw_from_deck_no_position(self):
        """DRAW_FROM_DECK should not have position."""
        action = Action(ActionType.DRAW_FROM_DECK)
        assert action.row is None
        assert action.col is None

    def test_draw_from_deck_with_position_fails(self):
        """DRAW_FROM_DECK with position should raise error."""
        with pytest.raises(ValueError):
            Action(ActionType.DRAW_FROM_DECK, row=1, col=2)

    def test_draw_from_discard_no_position(self):
        """DRAW_FROM_DISCARD should not have position."""
        action = Action(ActionType.DRAW_FROM_DISCARD)
        assert action.row is None
        assert action.col is None

    def test_swap_card_requires_position(self):
        """SWAP_CARD requires position."""
        action = Action(ActionType.SWAP_CARD, row=2, col=3)
        assert action.row == 2
        assert action.col == 3

    def test_swap_card_without_position_fails(self):
        """SWAP_CARD without position should fail."""
        with pytest.raises(ValueError):
            Action(ActionType.SWAP_CARD)

    def test_discard_and_flip_requires_position(self):
        """DISCARD_AND_FLIP requires position."""
        action = Action(ActionType.FLIP_CARD, row=0, col=1)
        assert action.row == 0
        assert action.col == 1

    def test_invalid_row_bounds(self):
        """Row out of bounds should raise error."""
        with pytest.raises(IndexError):
            Action(ActionType.SWAP_CARD, row=-1, col=0)

        with pytest.raises(IndexError):
            Action(ActionType.SWAP_CARD, row=3, col=0)

    def test_invalid_col_bounds(self):
        """Column out of bounds should raise error."""
        with pytest.raises(IndexError):
            Action(ActionType.SWAP_CARD, row=0, col=-1)

        with pytest.raises(IndexError):
            Action(ActionType.SWAP_CARD, row=0, col=4)