from skyjo.game.constants import NBR_COL, NBR_ROWS, MIN_PLAYERS, MAX_PLAYERS
from skyjo.game.deck import Deck
from skyjo.game.board import Board
from skyjo.game.player import Player

from skyjo.game.action import ActionType




class GameState:
    def __init__(self, num_players: int, player_names: list[str] = None):
        if not MIN_PLAYERS <= num_players <= MAX_PLAYERS:
            raise ValueError(f"The number of player should be between {MIN_PLAYERS} and {MAX_PLAYERS}, is {num_players}")
        if player_names is not None and len(player_names) != num_players:
            raise ValueError(
                f"Expected {num_players} names, got {len(player_names)}"
            )
        self.deck = None
        self.discard = None
        self.phase = "setup"
        self.last_round = False
        self.last_drawn_card = None

        self.players = [Player(i, player_names[i] if player_names else None)
                        for i in range(num_players)]
        self.current_player_index = 0

    def setup_round(self) -> None:
        self.deck = Deck()
        self.discard = []
        self.last_drawn_card = None
        for player in self.players:
            cards = [self.deck.draw() for _ in range(NBR_COL*NBR_ROWS)]
            board = Board(cards)
            player.set_board(board)
        self.discard.append(self.deck.draw())

    def get_current_player(self) -> Player:
        return self.players[self.current_player_index]

    def get_next_player(self) -> Player:
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return self.players[self.current_player_index]

    def get_valid_actions(self) -> list[ActionType]:
        if self.phase == "setup":
            return [ActionType.REVEAL_CARD]
        elif self.phase == "draw":
            return [ActionType.DRAW_FROM_DECK, ActionType.DRAW_FROM_DISCARD]
        elif self.phase == "post-draw":
            return [ActionType.SWAP_CARD, ActionType.FLIP_CARD]
        return []

    @property
    def round_over(self) -> bool:
        return self.round_over

    @property
    def game_over(self) -> bool:
        return self.game_over
    # def to_dict(self) -> dict  # For serialization