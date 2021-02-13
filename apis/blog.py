from flask_restx import Namespace, Resource, fields, reqparse
from database.blog import table as BLOGS
from bson.objectid import ObjectId
from flask import request
from datetime import datetime

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

blog_dto = api.model('BlogDetail', {
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


class BlogDTO(object):
  def __init__(self):
    self.title = None
    self.author = None
    self.content = None
    self.likes = 0
    self.shares = 0
    self.public = False
    self.tags= []
    self.category = 0
    self.date = None

  def get(self, id):
    blog = BLOGS.find_one({'_id': ObjectId(id)})
    if blog:
      return blog
    api.abort(404, 'Blog {} doesn\'t exit'.format(id))
  
  def create(self, payload):
    payload.update({
      'date': datetime.utcnow().isoformat(),
      'likes': 0,
      'shares': 0
    })
    blog_id = BLOGS.insert_one(payload).inserted_id
    
    return BLOGS.find_one({'_id': blog_id})

  def update(self, id, data):
    if BLOGS.find_one({'_id': ObjectId(id)}):
      BLOGS.update_one({
        '_id': ObjectId(id)
      }, {
        '$set': data
      })
      return { 'success': True }
      
    api.abort(404, 'Blog {} doesn\'t exit'.format(id))

  def delete(self,id):
    if BLOGS.find_one({'_id': ObjectId(id)}):
       BLOGS.delete_one({'_id': ObjectId(id)})
       return { 'success': True }
    api.abort(404, 'Blog {} doesn\'t exit'.format(id))

DTO = BlogDTO()


@api.route('/')
class BlogList(Resource):
  @api.doc('list_blogs')
  @api.marshal_list_with(blog)
  def get(self):
    '''List all blogs'''
    records = []
    for b in BLOGS.find():
      print(b)
      records.append(b)
    return records

  @api.doc('create_blog')
  @api.expect(blog_dto)
  @api.marshal_with(blog, code=201)
  def post(self):
    '''Create a blog'''
    return DTO.create(api.payload), 201
  


@api.route('/<id>')
@api.param('id', 'The blog identifier')
@api.response(404, 'Blog not found')
class Blog(Resource):
  @api.doc('get_blog')
  @api.marshal_with(blog)
  def get(self, id):
    '''Fetch a blog given its identifier'''
    return DTO.get(id)

  @api.doc('update_blog')
  @api.expect(blog_dto)
  def put(self, id):
    '''Update a blog with id'''
    return DTO.update(id, api.payload)

  def delete(self, id):
    '''Delete a blog with id'''
    return DTO.delete(id)