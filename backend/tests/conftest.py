import pytest
import random
from skyjo.game.card import Card

@pytest.fixture
def random_cards() -> list[Card]:
    """
    Generate 12 random cards for testing.

    Returns:
        List of 12 Card objects with random values (-2 to 12)
    """
    return [Card(random.randint(-2, 12)) for _ in range(12)]
