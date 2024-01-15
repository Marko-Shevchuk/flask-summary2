from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from app.api.games.controller import GameController, GamesController

games = Blueprint('games', __name__)

api = Api(games, errors=games.app_errorhandler)
api.add_resource(GameController, "/", "/<int:id>")
api.add_resource(GamesController, "/list")

@games.app_errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400


