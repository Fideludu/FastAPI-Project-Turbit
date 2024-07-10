import os
from pymongo import MongoClient
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

MONGODB_URI: Optional[str] = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
DB_NAME: Optional[str] = os.getenv("DB_NAME", "jsonplaceholder")

"""
Connect to MongoDB
"""
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
