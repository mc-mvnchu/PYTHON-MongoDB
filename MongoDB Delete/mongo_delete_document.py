import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Broadway 1666" }

mycol.delete_one(myquery)

# Print the customers collection after the deletion:
for x in mycol.find():
    print(x)