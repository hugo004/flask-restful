from flask import Flask
from apis import api_bp
import database

app = Flask(__name__)
app.register_blueprint(api_bp)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')