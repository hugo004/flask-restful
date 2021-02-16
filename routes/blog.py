from flask_restx import Resource
from model.blog import Blog as BlogModel
from schema.blog import BlogSchema

blog_model = BlogModel()
schema = BlogSchema()
api = schema.ns

@api.route('')
class BlogList(Resource):
  @api.doc(params=schema.query['params'])
  @api.marshal_list_with(schema.response['list'])
  def get(self):
    '''List all blogs'''
    parser = schema.query['parser']
    args = { key: value for key, value in parser.parse_args().items() if value is not None }
    return  blog_model.blog_list(args)

  @api.doc('create_blog')
  @api.expect(schema.dto)
  @api.marshal_with(schema.response['detail'], code=201)
  def post(self):
    '''Create a blog'''
    return blog_model.create(api.payload), 201
  


@api.route('/<id>')
@api.param('id', 'The blog identifier')
@api.response(404, 'Blog not found')
class Blog(Resource):
  @api.doc('get_blog')
  @api.marshal_with(schema.response['detail'])
  def get(self, id):
    '''Fetch a blog given its identifier'''
    blog = blog_model.get(id)
    if blog:
      return blog
    api.abort(404, 'Blog {} doesn\'t exit'.format(id))

  @api.doc('update_blog')
  @api.expect(schema.response['detail'])
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
