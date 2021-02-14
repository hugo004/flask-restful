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


  def blog_list(self):
    records = []
    for b in DB.find():
      records.append(b)
    return records

  def get(self, id):
    blog = DB.find_one({'_id': ObjectId(id)})
    if blog:
      return blog
  
  def create(self, payload):
    payload.update({
      'date': datetime.utcnow().isoformat(),
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
