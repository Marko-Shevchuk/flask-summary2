from marshmallow import fields, validate

from app import mm
from app.api.games.entity import Game


class GamesSchema(mm.SQLAlchemySchema):
    class Meta:
        model = Game
        load_instance = True
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True, validate=[validate.Length(1,128)])
    description = fields.String(required=False, validate=[validate.Length(max=2048)])
    size = fields.Float(required=True, validate=[validate.Range(min=0, max=100000)])
    publisher = fields.String(required=True, validate=[validate.Length(1,128)])