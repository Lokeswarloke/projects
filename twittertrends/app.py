from flask import Flask
from app.config import Config
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(Config)

client = MongoClient(Config.MONGODB_URI)
db = client[Config.MONGODB_DB]
collection = db[Config.MONGODB_COLLECTION]

from app import routes