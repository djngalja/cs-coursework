from uuid import UUID
from dataclasses import dataclass

from web.model.game_board_web import GameBoardWeb

@dataclass
class CurrentGameWeb:
    game_uuid: UUID
    board: GameBoardWeb
    game_state: str
    player1: UUID | None = None
    player2: UUID | None = None
    current_player: UUID | None = None
    winner: str | None = None
