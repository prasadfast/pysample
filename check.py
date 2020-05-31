import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
print(client)
db = client['test-database']

a = { "name": [''], "address": {"street": [''], "lane": ['']},"designation": [''] }

name = input("enter name:")
street = input("enter street:")
lane = input("enter the lane:")
designation = input("enter the designation:")
a["name"] = name
a["address"]["street"] = street
a["address"]["lane"] =  lane
a["designation"] = designation
posts = db.posts
post_id = posts.insert_one(a).inserted_id

print(a)
