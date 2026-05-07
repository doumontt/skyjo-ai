from skyjo.game.action import Action
from skyjo.game.game_state import GameState
from skyjo.game.player import Player


class Game:

    def __init__(self, num_players: int, player_names: list[str] = None):
        self.game_state = GameState(num_players, player_names)

    def start_game(self) -> None:
        """Start a new Skyjo Game"""
        self.game_state.current_player = self.game_state.players[0]

    def execute_action(self, action: Action) -> None:
        if action not in self.game_state.get_valid_actions():
            raise ValueError(f"Can't execute the action {action} given the current state of the game")
        # match action:
        #     case


    def end_turn(self) -> None:
        pass

    def end_round(self) -> None:
        """Finish the current Round, count points and reset the deck"""

    def start_new_round(self) -> None:
        """Reset the players board"""

    def get_winner(self) -> Player:
        """If the game is finished return the winner"""
        if not self.game_state.game_over:
            raise ValueError("We can't get a winner if hte game isn't over")
        return min(self.game_state.players, key=lambda obj: obj.total_score)

    def get_state(self) -> GameState:
        return self.game_state