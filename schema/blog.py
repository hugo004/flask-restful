from flask_restx import Namespace, fields

api = Namespace('blogs', description='Blogs related operations')

blog_list = api.model('BlogList', {
  '_id': fields.String(required=True, description='The blog identifier'),
  'title': fields.String(required=True, description='Blog title'),
  'author': fields.String(required=True, description='The blog author'),
  'content': fields.String(required=True, description='The blog\'s content'),
  'likes': fields.Integer(description='Number of like'),
  'shares': fields.Integer(description='Number of share'),
  'public': fields.Boolean(description='Is the blog pulish'),
  'tags': fields.List(fields.String, description="The blog tags"),
  'category': fields.Integer(description='The blog category'),
  'date': fields.DateTime(description='The blog creation date')
})

blog_detail = api.model('BlogDetail', {
  'title': fields.String(required=True, description='Blog title'),
  'author': fields.String(required=True, description='The blog author'),
  'content': fields.String(required=True, description='The blog\'s content'),
  'likes': fields.Integer(description='Number of like'),
  'shares': fields.Integer(description='Number of share'),
  'public': fields.Boolean(description='Is the blog pulish'),
  'tags': fields.List(fields.String, description="The blog tags"),
  'category': fields.Integer(description='The blog category'),
  'date': fields.DateTime(description='The blog creation date')
})