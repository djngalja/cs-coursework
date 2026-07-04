import uuid

from datasource.repository.service_interface import ServiceInterfaceDs
from datasource.repository.repository import Repository
from domain.model.current_game import CurrentGame
from domain.service.service_impl import ServiceInterface
from web.route.exceptions import GameNotFoundException, InvalidGameException, GameOverException

class ServiceImplDs(ServiceInterfaceDs):
    def __init__(self, repo: Repository, service: ServiceInterface):
        self.repository = repo
        self.service = service
    
    def create_game(self) -> CurrentGame:
        new_game = self.service.new_game()
        self.repository.save_game(new_game)
        return new_game
    
    def update_game(self, uuid: uuid.UUID, user_game: CurrentGame) -> CurrentGame:
        saved_game = self.get_game(uuid)
        if saved_game.game_over == True:
            raise GameOverException
        if not self.service.validate_current_game_board(saved_game, user_game):
            raise InvalidGameException
        if self.service.game_over_check(user_game):
            user_game.game_over = True
            self.repository.save_game(user_game)
            raise GameOverException
        next_move = self.service.next_move(user_game)
        self.service.apply_changes(user_game, next_move)
        if self.service.game_over_check(user_game):
            user_game.game_over = True
            self.repository.save_game(user_game)
            raise GameOverException
        self.repository.save_game(user_game)
        return user_game
    
    def get_game(self, uuid: uuid.UUID) -> CurrentGame:
        saved_game = self.repository.retrieve_game(uuid)
        if saved_game is None:
            raise GameNotFoundException
        return saved_game