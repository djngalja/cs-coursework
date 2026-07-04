from datasource.model.current_game_ds import CurrentGameDs
from domain.model.current_game import CurrentGame
from datasource.mapper.game_board_mapper import GameBoardMapper

class CurrentGameMapper:
    @staticmethod
    def domain_to_datasource(current_game: CurrentGame) -> CurrentGameDs:
        uuid = current_game.uuid
        board = GameBoardMapper.domain_to_datasource(current_game.board)
        game_over = current_game.game_over
        return CurrentGameDs(uuid, board, game_over)
    
    @staticmethod
    def datasource_to_domain(current_game_ds: CurrentGameDs) -> CurrentGame:
        uuid = current_game_ds.uuid
        board = GameBoardMapper.datasource_to_domain(current_game_ds.board)
        game_over = current_game_ds.game_over
        return CurrentGame(uuid, board, game_over)