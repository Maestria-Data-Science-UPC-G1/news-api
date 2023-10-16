from marshmallow import fields

#from app.ext import ma
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class FilmSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    length = fields.Integer()
    year = fields.Integer()
    director = fields.String()
    actors = fields.Nested('ActorSchema', many=True)


class ActorSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()

class NewSchema(ma.Schema):
    # elemento data de tipo DataSchema
    data = fields.Nested('DataSchema')

class DataSchema(ma.Schema):
    nodes = fields.Nested('NodeSchema', many=True)
    links = fields.Nested('LinkSchema', many=True)

class NodeSchema(ma.Schema):
    title = fields.String()
    content = fields.String()
    url = fields.String()

class LinkSchema(ma.Schema):
    source = fields.String()
    target = fields.String()
    value = fields.Integer()
    
class Link:
    def __init__(self, source, target, value):
        self.source = source
        self.target = target
        self.value = value

    def __dict__(self):
        return {
            'source': self.source,
            'target': self.target,
            'value': self.value
        }

class Node:
    def __init__(self, id, title, content, url, author, description, published_at, group):
        self.id = id
        self.title = title
        self.content = content
        self.url = url
        self.author = author
        self.description = description
        self.published_at = published_at
        self.group = group

    def __dict__(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'url': self.url,
            'author': self.author,
            'description': self.description,
            'published_at': self.published_at,
            'group': self.group
        }