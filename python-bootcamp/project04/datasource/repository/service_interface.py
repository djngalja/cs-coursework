from abc import ABC, abstractmethod
import uuid

from domain.model.current_game import CurrentGame

class ServiceInterfaceDs(ABC):
    @abstractmethod
    def create_game(self) -> CurrentGame:
        pass

    @abstractmethod
    def update_game(self, uuid: uuid.UUID, user_game: CurrentGame) -> CurrentGame:
        pass

    @abstractmethod
    def get_game(self, uuid: uuid.UUID) -> CurrentGame:
        pass