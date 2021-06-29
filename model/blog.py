from datetime import datetime
from database.blog import table as DB
from bson.objectid import ObjectId

class Blog(object):
  def __init__(self):
    self.title = None
    self.author = None
    self.content = None
    self.likes = 0
    self.shares = 0
    self.public = False
    self.tags= []
    self.category = 0
    self.date = None


  def blog_list(self, query):
    
    cursor = None
    if 'startTime' and 'endTime' in query:
      cursor = DB.find({
        'date': { '$gte': query.get('startTime').isoformat(), '$lte': query.get('endTime').isoformat() }
      })
    elif 'startTime' in query:
      cursor = DB.find({
        'date': { '$gte': query.get('startTime').isoformat() }
      })
    elif 'endTime' in query:
      cursor = DB.find({
        'date': { '$lte':  query.get('endTime').isoformat() }
      })
    else:
      cursor = DB.find()

    size = query.get('pageSize', 10)
    page = query.get('page', 1)
    skip = (page-1) * size

    return {
      'items': [ record for record in cursor.skip(skip).limit(size) ],
      'page': page,
      'pageSize': size
    }

  def get(self, id):
    blog = DB.find_one({'_id': ObjectId(id)})
    if blog:
      return blog
  
  def create(self, payload):
    payload.update({
      'date': datetime.now().replace(microsecond=0).isoformat(),
      'likes': 0,
      'shares': 0
    })
    blog_id = DB.insert_one(payload).inserted_id
    
    return DB.find_one({'_id': blog_id})

  def update(self, id, data):
    if DB.find_one({'_id': ObjectId(id)}):
      DB.update_one({
        '_id': ObjectId(id)
      }, {
        '$set': data
      })
      return { 'success': True }
      

  def delete(self,id):
    if DB.find_one({'_id': ObjectId(id)}):
       DB.delete_one({'_id': ObjectId(id)})
       return { 'success': True }
