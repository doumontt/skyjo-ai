from skyjo.game.board import Board

class Player:
    """
    Class representing a specific player
    Attributes:
        board: The board of this player
        _total_score: The total score of this player in this game
    """

    def __init__(self, player_id: int, name: str = None):
        self.board = None
        self.player_id = player_id
        self.name = name if name else f"Player {player_id}"
        self._total_score = 0

    def set_board(self, board: Board):
        """Set the Board of this player to board"""
        self.board = board

    @property
    def total_score(self) -> int:
        """Return the current score of this player"""
        return self._total_score

    def get_current_score(self) -> int:
        """ Return the value of this player's Board, ie: the sum of its cards"""
        if self.board is None:
            raise ValueError(f"Player {self.player_id} has no board set")
        return sum(card.value for card in self.board.get_all_cards()
                    if card is not None)


    def add_score(self, score: int) -> None:
        """Update the total_score of this player by adding score"""
        if not isinstance(score, int):
            raise TypeError(f"Score must be an integer, got an {type(score)}")
        self._total_score += score

    def has_all_revealed(self) -> bool:
        """Return True if all the cards from this player are revealed"""
        return self.board.all_revealed()

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"{self.name} (ID: {self.player_id}, Score: {self.total_score})"

    def __repr__(self) -> str:
        """Developer representation."""
        return f"Player(player_id={self.player_id}, name='{self.name}', total_score={self.total_score})"