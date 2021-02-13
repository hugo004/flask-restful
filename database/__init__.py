from pymongo import MongoClient

db_connect_str = 'mongodb+srv://dbAdmin:123qwe@cluster0.w82b5.mongodb.net/blog_db?retryWrites=true&w=majority'
client = MongoClient(db_connect_str)