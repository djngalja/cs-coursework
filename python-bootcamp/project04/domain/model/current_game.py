import uuid
from dataclasses import dataclass

from domain.model.game_board import GameBoard

@dataclass
class CurrentGame:
    uuid: uuid.UUID
    board: GameBoard
    game_over: bool = False