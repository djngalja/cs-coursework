from flask import Blueprint, jsonify, request
import uuid

from di.container import get_container
from web.mapper.current_game_mapper import CurrentGameMapper
from web.model.current_game_web import CurrentGameWeb, GameBoardWeb
from web.route.exceptions import GameNotFoundException, InvalidGameException, GameOverException

bp = Blueprint("game", __name__)

@bp.route("/game", methods=["POST"])
def create_game():
    container = get_container()
    game = container.get_repo_service().create_game()
    return jsonify(CurrentGameMapper.domain_to_web(game).__dict__), 200

@bp.route("/game/<current_game_UUID>", methods=["POST"])
def update_game(current_game_UUID: uuid.UUID):
    container = get_container()
    user_input = request.get_json(silent=True)
    if (not user_input or "state" not in user_input):
        return jsonify({"error": "Invalid input format"}), 400 
    board = GameBoardWeb(user_input["state"])
    game_web = CurrentGameWeb(current_game_UUID, board)
    game = CurrentGameMapper.web_to_domain(game_web)
    try:
        upd_game = container.get_repo_service().update_game(current_game_UUID, game)
    except GameNotFoundException:
        return jsonify({"error": f"Game <{current_game_UUID}> not found"}), 400 
    except InvalidGameException:
        return jsonify({"error": "Invalid board submitted"}), 400 
    except GameOverException:
        final_game = container.get_repo_service().get_game(current_game_UUID)
        response = CurrentGameMapper.domain_to_web(final_game).__dict__
        response["message"] = "Game Over"
        return jsonify(response), 200
    return jsonify(CurrentGameMapper.domain_to_web(upd_game).__dict__), 200