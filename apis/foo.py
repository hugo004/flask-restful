
from flask_restx import Api, Namespace, Resource, fields


ns = Namespace('Foo', description='Foo related operations')
foo = ns.model('Foo', {
  'id': fields.String(required=True, description='The foo identifier'),
  'title': fields.String(required=True, description='foo title')
})

# api.add_namespace(ns)

FOOS = [
  { 'id': '1', 'title': 'blog' }
]

@ns.route('/')
class BlogList(Resource):
  @ns.doc('list_foos')
  @ns.marshal_list_with(foo)
  def get(self):
    '''List all blogs'''
    return FOOS

