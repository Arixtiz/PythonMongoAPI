from pymongo import MongoClient
import os 

conn = MongoClient(os.getenv("DATABASE_CONN"))
db = conn[os.getenv("DATABASE_NAME")]