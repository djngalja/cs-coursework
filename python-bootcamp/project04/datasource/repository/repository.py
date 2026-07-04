import uuid

from datasource.repository.game_storage import GameStorage
from domain.model.current_game import CurrentGame
from datasource.mapper.current_game_mapper import CurrentGameMapper

class Repository:
    def __init__(self, storage: GameStorage):
        self.storage = storage

    def save_game(self, current_game: CurrentGame) -> None:
        current_game_ds = CurrentGameMapper.domain_to_datasource(current_game)
        self.storage.save_game(current_game_ds)

    def retrieve_game(self, uuid: uuid.UUID) -> CurrentGame | None:
        current_game_ds = self.storage.get_game(uuid)
        if current_game_ds is None:
            return None
        current_game = CurrentGameMapper.datasource_to_domain(current_game_ds)
        return current_game