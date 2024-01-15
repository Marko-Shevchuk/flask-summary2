from flask import Blueprint
from app import basic_auth


auth = Blueprint('auth', __name__)

from . import controller

@basic_auth.error_handler
def handle_auth_error(status):
    return "Failure to authenticate", status

