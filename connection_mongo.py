from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

with open('apiConnection.json') as file:
    data = json.load(file)

uri = data["uri"]

clientMongo = MongoClient(uri, server_api=ServerApi('1'))