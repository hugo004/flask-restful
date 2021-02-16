from flask_restx import fields

class BaseSchema(object):
  def base_response(self, model):
    return {
      'items': fields.List(fields.Nested(model)),
      'page': fields.Integer(description='current page'),
      'pageSize': fields.Integer(description='page size')
    }