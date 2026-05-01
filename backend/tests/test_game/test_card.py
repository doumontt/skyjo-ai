"""Tests for Card class"""

import pytest
from backend.skyjo.game.card import Card


class TestCard:
    def test_card_creation(self):
        """Test basic card creation."""
        card = Card(value=5)
        assert card.value == 5
        assert card.revealed is False

    def test_card_value_range(self):
        """Test valid card values."""
        # Valid cards
        Card(value=-2)  # Should not raise
        Card(value=0)  # Should not raise
        Card(value=12)  # Should not raise

        # Invalid cards
        with pytest.raises(ValueError):
            Card(value=-3)

        with pytest.raises(ValueError):
            Card(value=13)

    def test_card_string_representation(self):
        """Test string output for hidden and revealed cards."""
        hidden = Card(value=7, revealed=False)
        revealed = Card(value=7, revealed=True)

        assert "?" in str(hidden)
        assert "7" in str(revealed)

    @pytest.mark.parametrize("value", [-2, -1, 0, 1, 5, 10, 12])
    def test_all_valid_card_values(self, value):
        """Test all valid card values can be created."""
        card = Card(value=value)
        assert card.value == value
