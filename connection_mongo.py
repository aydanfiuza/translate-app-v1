from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://aydanfiuza:shggwu2009@translate-app.6ffsthk.mongodb.net/?retryWrites=true&w=majority"

clientMongo = MongoClient(uri, server_api=ServerApi('1'))