import config
import datetime
import jwt
 
class Auth (object):
  def __init__(self):
    pass

def encode(self, user_id):
  try:
    payload = {
      'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
      'iat': datetime.datetime.utcnow(),
      'sub': user_id
    }

    return jwt.encode(payload, config.SECRET_KEY)
  except jwt.ExpiredSignatureError:
    return 'expired'
  except jwt.InvalidTokenError:
    return 'invalid token'

def decode(self):
  pass
