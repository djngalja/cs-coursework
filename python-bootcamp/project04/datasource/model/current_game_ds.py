import uuid
from dataclasses import dataclass

from datasource.model.game_board_ds import GameBoardDs

@dataclass
class CurrentGameDs:
    uuid: uuid.UUID
    board: GameBoardDs
    game_over: bool = False