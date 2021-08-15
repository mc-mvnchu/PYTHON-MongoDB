import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# For loop to specific requested fields, i.e the `names` and `addresses`, not the _ids
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
    print(x)