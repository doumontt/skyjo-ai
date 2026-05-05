"""Tests for Deck class"""
import random

import pytest
from mypy.nodes import PASS_STMT

from skyjo.game.deck import Deck
from skyjo.game.constants import CARD_DISTRIBUTION


class TestDeck:
    def test_deck_creation(self):
        """Test basic deck creation"""
        deck = Deck()
        assert deck.cards_remaining() == 150

    def test_draw(self):
        """Test drawing of a card"""
        deck = Deck()
        card = deck.draw()
        assert card is not None

    def test_card_distribution(self):
        """Test that the distribution of the cards is correct"""
        deck = Deck()
        deck.shuffle()
        dic = {}
        for _ in range(150):
            val = deck.draw().value
            dic[val] = dic.get(val, 0) +1
        assert dic == CARD_DISTRIBUTION

    def test_draw_from_empty(self):
        """Check that trying to draw a card from an empty deck raises an error"""
        deck = Deck()
        for _ in range(150):
            deck.draw()
        with pytest.raises(IndexError):
            deck.draw()

    def test_shuffle(self):
        """Check that the shuffle works correctly"""
        random.seed(10)
        values = []
        for _ in range(10):
            deck = Deck()
            deck.shuffle()
            values.append(deck.draw().value)
        assert len({value for value in values}) != 1

    def test_is_empty(self):
        """Chech that the function is_empty return true when the deck is empty, false otherwise"""
        deck = Deck()
        for _ in range(50):
            deck.draw()
        assert not deck.is_empty()
        for _ in range(100):
            deck.draw()
        assert deck.is_empty()


    def test_cards_remaining(self):
        """Check that the function cards-remaining returns the correct number of cards"""
        deck = Deck()
        for _ in range(50):
            deck.draw()
        assert deck.cards_remaining() == 100
        for _ in range(100):
            deck.draw()
        assert deck.cards_remaining() == 0

