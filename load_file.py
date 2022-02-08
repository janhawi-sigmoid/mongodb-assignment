from pymongo import MongoClient
import json
from bson import ObjectId

try:
    client = MongoClient('localhost', 27017)
    print("Connected")
except:
    print("Print could not connect to MongoDB")

# creating database
db = client['sample_mflix']

#creating collection
# Q2. Bulk load the JSON files in the individual MongoDB collections using Python
# a. Load comments
collection_comments = db['comments']
comment_list=[]

with open('/Users/janhawishresth/Desktop/sample_mflix/comments.json') as f:
    for obj in f:
        if obj:
            my_dict = json.loads(obj)
            my_dict["_id"] = ObjectId(my_dict["_id"]["$oid"])
            my_dict["date"] = my_dict["date"]["$date"]["$numberLong"]
            comment_list.append(my_dict)

collection_comments.insert_many(comment_list)

# b. Load movies
collection_movies = db['movies']
movies_list = []

with open('/Users/janhawishresth/Desktop/sample_mflix/movies.json') as f:
    for obj in f:
        if obj:
            my_dict = json.loads(obj)
            my_dict["_id"] = ObjectId(my_dict["_id"]["$oid"])
            movies_list.append(my_dict)

collection_movies.insert_many(movies_list)

# c. Load Theaters
collection_theaters = db['theaters']
theater_list = []

with open('/Users/janhawishresth/Desktop/sample_mflix/theaters.json') as f:
    for obj in f:
        if obj:
            my_dict = json.loads(obj)
            my_dict["_id"] = ObjectId(my_dict["_id"]["$oid"])
            my_dict["location"]["geo"]["coordinates"][0] = float(my_dict["location"]["geo"]["coordinates"][0]["$numberDouble"])
            my_dict["location"]["geo"]["coordinates"][1] = float(my_dict["location"]["geo"]["coordinates"][1]["$numberDouble"])
            theater_list.append(my_dict)

collection_theaters.insert_many(theater_list)

# d. Load users
collection_users = db['users']
users_list = []

with open('/Users/janhawishresth/Desktop/sample_mflix/users.json') as f:
    for obj in f:
        if obj:
            my_dict = json.loads(obj)
            my_dict["_id"] = ObjectId(my_dict["_id"]["$oid"])
            users_list.append(my_dict)

collection_users.insert_many(users_list)