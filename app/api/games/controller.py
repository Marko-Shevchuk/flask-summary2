from flask import request
from flask_restful import Resource

from app import db
from app.api.auth.jwt_utils import JWTUtils
from app.api.games.entity import Game
from app.api.games.schemes import GamesSchema


class GameController(Resource):
    @JWTUtils.verify_token
    def get(self, id):
        game = Game.query.get(id)
        return GamesSchema().dump(game), 200

    @JWTUtils.verify_token
    def post(self):
        schema = GamesSchema()
        entity = schema.load(request.json)
        db.session.add(entity)
        db.session.commit()
        return schema.dump(entity), 201

    @JWTUtils.verify_token
    def put(self, id):
        game = Game.query.get(id)
        schema = GamesSchema()
        entity = schema.load(request.json, instance=game)
        db.session.commit()
        return schema.dump(entity), 200

    @JWTUtils.verify_token
    def delete(self, id):
        game = Game.query.get(id)
        db.session.delete(game)
        db.session.commit()
        return {}, 204



class GamesController(Resource):
    @JWTUtils.verify_token
    def get(self):
        return GamesSchema(many=True).dump(Game.query.all())
