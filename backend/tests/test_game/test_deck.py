"""Tests for Deck class"""
import random

import pytest

from skyjo.game.deck import Deck
from skyjo.game.constants import CARD_DISTRIBUTION, TOTAL_CARDS


class TestDeck:
    def test_deck_creation(self):
        """Test basic deck creation"""
        deck = Deck()
        assert deck.cards_remaining() == TOTAL_CARDS

    def test_deck_contains_card_objects(self):
        """Deck should contain Card objects."""
        from skyjo.game.card import Card

        deck = Deck()
        card = deck.draw()

        assert isinstance(card, Card)
        assert hasattr(card, 'value')
        assert hasattr(card, 'revealed')

    def test_draw(self):
        """Test drawing of a card"""
        deck = Deck()
        card = deck.draw()
        assert card is not None

    def test_card_distribution(self):
        """Test that the distribution of the cards is correct"""
        deck = Deck()
        dic = {}
        for _ in range(150):
            val = deck.draw().value
            dic[val] = dic.get(val, 0) +1
        assert dic == CARD_DISTRIBUTION

    def test_draw_from_empty(self):
        """Check that trying to draw a card from an empty deck raises an error"""
        deck = Deck()
        for _ in range(TOTAL_CARDS):
            deck.draw()
        with pytest.raises(IndexError, match="Cannot draw from empty deck"):
            deck.draw()

    def test_deck_shuffled_on_creation(self):
        """Deck should be automatically shuffled upon creation."""
        # Two decks created with different seeds should have different orders
        random.seed(1)
        deck1 = Deck()
        first_cards_1 = [deck1.draw().value for _ in range(5)]

        random.seed(2)
        deck2 = Deck()
        first_cards_2 = [deck2.draw().value for _ in range(5)]

        assert first_cards_1 != first_cards_2

    def test_shuffle(self):
        random.seed(42)
        deck1 = Deck()
        first_10_cards = [deck1.draw().value for _ in range(10)]

        random.seed(42)
        deck2 = Deck()
        deck2.shuffle()
        second_10_cards = [deck2.draw().value for _ in range(10)]

        assert first_10_cards != second_10_cards

    def test_is_empty(self):
        """Check that the function is_empty return true when the deck is empty, false otherwise"""
        deck = Deck()
        for _ in range(50):
            deck.draw()
        assert not deck.is_empty()
        for _ in range(TOTAL_CARDS-50):
            deck.draw()
        assert deck.is_empty()


    def test_cards_remaining(self):
        """Check that the function cards-remaining returns the correct number of cards"""
        deck = Deck()
        for _ in range(50):
            deck.draw()
        assert deck.cards_remaining() == TOTAL_CARDS-50
        for _ in range(TOTAL_CARDS-50):
            deck.draw()
        assert deck.cards_remaining() == 0

