import requests
from pymongo import MongoClient

"""
Connect to MongoDB
"""
client = MongoClient("mongodb://localhost:27017/")
db = client["jsonplaceholder"]

"""
 Function to load data from an endpoint
"""


def load_data(endpoint, collection_name):
    response = requests.get(f"https://jsonplaceholder.typicode.com/{endpoint}")
    data = response.json()
    collection = db[collection_name]
    collection.insert_many(data)


"""
Load posts and comments into MongoDB
"""
load_data("posts", "posts")
load_data("comments", "comments")
load_data("users", "users")

print("Data loaded successfully")
