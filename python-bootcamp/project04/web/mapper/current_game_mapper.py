from web.model.current_game_web import CurrentGameWeb
from domain.model.current_game import CurrentGame
from web.mapper.game_board_mapper import GameBoardMapper

class CurrentGameMapper:
    @staticmethod
    def domain_to_web(current_game: CurrentGame) -> CurrentGameWeb:
        uuid = current_game.uuid
        board = GameBoardMapper.domain_to_web(current_game.board)
        game_over = current_game.game_over
        return CurrentGameWeb(uuid, board, game_over)
    
    @staticmethod
    def web_to_domain(current_game_web: CurrentGameWeb) -> CurrentGame:
        uuid = current_game_web.uuid
        board = GameBoardMapper.web_to_domain(current_game_web.board)
        game_over = current_game_web.game_over
        return CurrentGame(uuid, board, game_over)