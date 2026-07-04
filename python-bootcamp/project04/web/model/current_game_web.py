import uuid
from dataclasses import dataclass

from web.model.game_board_web import GameBoardWeb

@dataclass
class CurrentGameWeb:
    uuid: uuid.UUID
    board: GameBoardWeb
    game_over: bool = False