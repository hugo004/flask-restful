from flask_restx import Namespace, fields, reqparse, inputs
from . import base_response

api = Namespace('blogs', description='Blogs related operations')

blog_base = api.model('BlogBase', {
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

detail_response = api.clone('BlogDetail', {
  '_id': fields.String(required=True, description='The blog identifier'),
}, blog_base)


list_response = api.model('BlogList', base_response(detail_response))



# query params setting
blog_query = reqparse.RequestParser()
blog_query.add_argument('title', type=str)
blog_query.add_argument('author', type=str)
blog_query.add_argument('category', type=int)
blog_query.add_argument('date', type=inputs.date_from_iso8601)
blog_query.add_argument('page', type=int, default=1)
blog_query.add_argument('pageSize', type=int, default=10)

blog_query_params = {
  'title': { 'description': 'Blog title', 'type': 'string' },
  'author': { 'description': 'Blog author', 'type': 'string' },
  'category': { 'description': 'Blog category', 'type': 'integer($int32)', 'default': 0 },
  'date': { 'description': 'Blog created time', 'type': 'string($date-time)' },
  'page': { 'type': 'integer($int32)' },
  'pageSize': { 'type': 'integer($int32)' }
}
