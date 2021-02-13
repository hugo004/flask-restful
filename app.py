# from flask import Flask
# from apis import api

# app = Flask(__name__)
# api.init_app(app)

# if __name__ == '__main__':
#   app.run(debug=True)


from flask import Flask
# from apis.foo import api_bp
from apis import api_bp
import database

app = Flask(__name__)
app.register_blueprint(api_bp)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')