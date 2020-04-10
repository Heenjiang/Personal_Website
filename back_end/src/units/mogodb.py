from pymongo import MongoClient
client = MongoClient('mongodb://myUserAdmin:abc123@localhost/')
db = client.pwdb
