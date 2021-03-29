from Configs import Config
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    mongo_client = MongoClient(Config.MONGO_DB)
    mongo_client.server_info()
except ConnectionFailure:
    print("Invalid Mongo DB URL. Please Check Your Credentials!")
    quit(1)
