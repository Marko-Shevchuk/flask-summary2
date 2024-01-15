from flask import Flask
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mm = Marshmallow()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.secret_key = b'agueguedasdewrf'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)
    mm.init_app(app)
    bcrypt.init_app(app)
    return app


app = create_app()
Migrate(app, db)
