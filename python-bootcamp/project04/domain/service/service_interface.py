from abc import ABC, abstractmethod

from domain.model.current_game import CurrentGame

class ServiceInterface(ABC):
    @abstractmethod
    def next_move(self, current_game: CurrentGame) -> tuple[int, int]:
        pass

    @abstractmethod
    def validate_current_game_board(self, game: CurrentGame, user_game: CurrentGame) -> bool:
        pass

    @abstractmethod
    def game_over_check(self, current_game: CurrentGame) -> bool:
        pass

    @abstractmethod
    def new_game(self) -> CurrentGame:
        pass

    @abstractmethod
    def apply_changes(self, current_game: CurrentGame, move: tuple[int, int]) -> None:
        pass