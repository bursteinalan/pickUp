from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
client.test_database
db = client['test-database']
