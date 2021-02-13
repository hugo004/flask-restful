from . import client

db = client.get_database('blog_db')
table = db['blog_records']