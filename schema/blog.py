from flask_restx import Namespace, fields, reqparse, inputs
from .baseSchema import BaseSchema


class BlogSchema(BaseSchema):
  def __init__(self):
    ns = Namespace('blogs', description='Blogs related operations')

    # private variables
    __base = ns.model('BlogBase', {
      'date': fields.DateTime(description='The blog creation date'),
      'title': fields.String(required=True, description='Blog title'),
      'author': fields.String(required=True, description='The blog author'),
      'content': fields.String(required=True, description='The blog\'s content'),
      'likes': fields.Integer(description='Number of like'),
      'shares': fields.Integer(description='Number of share'),
      'public': fields.Boolean(description='Is the blog pulish'),
      'category': fields.Integer(description='The blog category', enum=[0, 1, 2, 3]),
      'tags': fields.List(fields.String, description="The blog tags")
    })
    __detail = ns.clone('BlogDetail', {
      '_id': fields.String(required=True, description='The blog identifier'),
    }, __base)
    __list = ns.model('BlogList', self.base_response(__detail))

    # query params setting
    __params = {
      'title': { 'description': 'Blog title', 'type': 'string' },
      'author': { 'description': 'Blog author', 'type': 'string' },
      'category': { 'description': 'Blog category', 'type': 'integer($int32)', 'default': 0 },
      'date': { 'description': 'Blog created time', 'type': 'string($date-time)' },
      'page': { 'type': 'integer($int32)' },
      'pageSize': { 'type': 'integer($int32)' }
    }

    __parser = reqparse.RequestParser()
    __parser.add_argument('title', type=str)
    __parser.add_argument('author', type=str)
    __parser.add_argument('category', type=int)
    __parser.add_argument('date', type=inputs.date_from_iso8601)
    __parser.add_argument('page', type=int, default=1)
    __parser.add_argument('pageSize', type=int, default=10)
    
    # public variables
    self.ns = ns
    self.dto = __base

    self.response = {
      'list': __list,
      'detail': __detail
    }
    self.query = {
      'parser': __parser,
      'params': __params
    }
