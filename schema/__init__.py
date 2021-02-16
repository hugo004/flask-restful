from flask_restx import fields

def base_response(model):
  return {
    'items': fields.List(fields.Nested(model)),
    'page': fields.Integer(description='current page'),
    'pageSize': fields.Integer(description='page size')
  }