# from flask_restx import Api
# from .blog import api as blog_ns

# api = Api(
#   title='Hugo Swagger',
#   version='1.0',
#   description='A simple api'
# )

# api.add_namespace(blog_ns, path='/api/v1/blogs')



from flask_restx import Api
from flask import Blueprint
from .foo import ns as foo_ns
from .blog import api as blog_ns

api_bp = Blueprint('api', __name__)
api = Api(
  api_bp,
  title='Hugo Swagger',
  version='1.0',
  description='A simple api'
)

api.add_namespace(blog_ns)
api.add_namespace(foo_ns)