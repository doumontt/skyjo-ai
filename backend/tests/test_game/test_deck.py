"""Tests for Deck class"""

import pytest
from mypy.nodes import PASS_STMT

from skyjo.game.deck import Deck
from skyjo.game.constants import CARD_DISTRIBUTION


class TestDeck:
    def test_deck_creation(self):
        deck = Deck()
        assert deck.cards_remaining() == 150

    def test_draw(self):
        deck = Deck()
        card = deck.draw()

        # assert

    def test_card_distribution(self):
        pass

    def test_draw_from_empty(self):
        deck = Deck()
        for _ in range(150):
            deck.draw()
        assert
        pass

    def test_shuffle(self):
        pass

    def test_is_empty(self):
        pass

    def test_cards_remaining(self):
        pass
