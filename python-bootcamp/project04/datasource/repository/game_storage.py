import uuid
import threading

from datasource.model.current_game_ds import CurrentGameDs

class GameStorage:
    def __init__(self):
        self.games: dict[str, CurrentGameDs] = {}
        self.lock = threading.RLock()

    def save_game(self, current_game_ds: CurrentGameDs) -> None:
        with self.lock:
            self.games[str(current_game_ds.uuid)] = current_game_ds

    def get_game(self, game_uuid: uuid.UUID) -> CurrentGameDs | None:
        return self.games.get(str(game_uuid))