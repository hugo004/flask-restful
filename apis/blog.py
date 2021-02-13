from flask_restx import Namespace, Resource, fields
from database.blog import table as BLOGS

api = Namespace('blogs', description='Blogs related operations')
blog = api.model('Blog', {
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

  def post(self):
    '''Create a blog'''
    pass
  


@api.route('/<id>')
@api.param('id', 'The blog identifier')
@api.response(404, 'Blog not found')
class Blog(Resource):
  @api.doc('get_blog')
  @api.marshal_list_with(blog)
  def get(self, id):
    '''Fetch a blog given its identifier'''
    blog = BLOGS.find_one({'_id': id})
    print(blog)
    if blog:
      return blog
    api.abort(404)

  def put(self, id):
    '''Update a blog with id'''
    pass

  def delete(self, id):
    '''Delete a blog with id'''
    pass