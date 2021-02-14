from flask_restx import Namespace, Resource, fields
from flask import request
from model.blog import Blog as BlogModel

blog_model = BlogModel()

api = Namespace('blogs', description='Blogs related operations')
blog = api.model('BlogList', {
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

blog_blog_model = api.model('BlogDetail', {
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


@api.route('/')
class BlogList(Resource):
  @api.doc('list_blogs')
  @api.marshal_list_with(blog)
  def get(self):
    '''List all blogs'''
    return  blog_model.blog_list()

  @api.doc('create_blog')
  @api.expect(blog_blog_model)
  @api.marshal_with(blog, code=201)
  def post(self):
    '''Create a blog'''
    return blog_model.create(api.payload), 201
  


@api.route('/<id>')
@api.param('id', 'The blog identifier')
@api.response(404, 'Blog not found')
class Blog(Resource):
  @api.doc('get_blog')
  @api.marshal_with(blog)
  def get(self, id):
    '''Fetch a blog given its identifier'''
    blog = blog_model.get(id)
    if blog:
      return blog
    api.abort(404, 'Blog {} doesn\'t exit'.format(id))

  @api.doc('update_blog')
  @api.expect(blog_blog_model)
  def put(self, id):
    '''Update a blog with id'''
    success = blog_model.update(id, api.payload)
    if success:
      return success
    api.abort(404, 'Blog {} doesn\'t exit'.format(id))

  def delete(self, id):
    '''Delete a blog with id'''
    success = blog_model.delete(id)
    if success:
      return success
    api.abort(404, 'Blog {} doesn\'t exit'.format(id))
