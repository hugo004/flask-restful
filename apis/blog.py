from flask_restx import Resource
from model.blog import Blog as BlogModel
from schema.blog import api, blog_base, list_response, detail_response, blog_query_params, blog_query

blog_model = BlogModel()

@api.route('')
class BlogList(Resource):
  @api.doc(params=blog_query_params)
  @api.marshal_list_with(list_response)
  def get(self):
    '''List all blogs'''
    args = { key: value for key, value in blog_query.parse_args().items() if value is not None }
    return  blog_model.blog_list(args)

  @api.doc('create_blog')
  @api.expect(blog_base)
  @api.marshal_with(detail_response, code=201)
  def post(self):
    '''Create a blog'''
    return blog_model.create(api.payload), 201
  


@api.route('/<id>')
@api.param('id', 'The blog identifier')
@api.response(404, 'Blog not found')
class Blog(Resource):
  @api.doc('get_blog')
  @api.marshal_with(detail_response)
  def get(self, id):
    '''Fetch a blog given its identifier'''
    blog = blog_model.get(id)
    if blog:
      return blog
    api.abort(404, 'Blog {} doesn\'t exit'.format(id))

  @api.doc('update_blog')
  @api.expect(detail_response)
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
