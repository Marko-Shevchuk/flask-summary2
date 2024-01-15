from flask import Blueprint

from app.api.auth import auth
from app.api.games import games

api = Blueprint('api', __name__)
api.register_blueprint(auth, url_prefix='/auth')
api.register_blueprint(games, url_prefix='/game')